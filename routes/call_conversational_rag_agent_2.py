import json
import time
from datetime import datetime, timezone
import pydash
from clients.PineconeClient import PineconeClient

PineconeClient.connectPinecone()  # needs to be above the 'tools' import

from langchain.chat_models import ChatOpenAI
from langchain.load.dump import dumps
from langchain.agents import AgentExecutor
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.prompts import MessagesPlaceholder
from langchain.schema.messages import SystemMessage
from langchain.agents.openai_functions_agent.agent_token_buffer_memory import (
    AgentTokenBufferMemory,
)

# from agents.chat_with_docket_agent.memory import CustomAgentTokenBufferMemory

from langchain.memory import ChatMessageHistory

from agents.rag_agent_2.callback_handlers.custom_callback_handler import (
    CustomCallbackHandler,
)
from agents.rag_agent_2.helpers.save_agent_stats import save_agent_stats
from agents.rag_agent_2.tools import (
    BuildQueryTool,
    RunQueryTool,
    DocketApiTool,
    VectorStoreTool,
)
from flask import Blueprint, request, stream_with_context, Response
from basic_auth.index import auth

llm = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")

history = ChatMessageHistory()

tools = [
    VectorStoreTool,
    DocketApiTool,
    BuildQueryTool,
    RunQueryTool,
]

call_conversational_rag_agent_2_blueprint = Blueprint(
    "call_conversational_rag_agent_2", __name__
)


@call_conversational_rag_agent_2_blueprint.route(
    "/call_conversational_rag_agent_2", methods=["POST"]
)
# @auth.login_required
def call_conversational_rag_agent_2():
    def generate():
        print("entering R.A.G. agent #2 generate...")

        try:
            tic = time.perf_counter()
            content_type = request.headers.get("Content-Type")
            human_prompt = None
            if content_type == "application/json" and request.json:
                json_payload = request.json
                human_prompt = json_payload["prompt"]
            else:
                return "Content-Type not supported!"
            system_message = SystemMessage(
                content=(
                    "Do your best to answer the questions. Feel free to use any tools available to look up relevant information, only if necessary."
                )
            )
            # - vvv vvv vvv --- vvv vvv
            #    Chat Message History
            # - vvv vvv vvv --- vvv vvv
            memory_key = "history"
            memory = AgentTokenBufferMemory(
                memory_key=memory_key, llm=llm, chat_memory=history
            )

            prompt = OpenAIFunctionsAgent.create_prompt(
                system_message=system_message,
                extra_prompt_messages=[MessagesPlaceholder(variable_name=memory_key)],
            )
            agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)
            agent_executor = AgentExecutor(
                agent=agent,
                tools=tools,
                memory=memory,
                return_intermediate_steps=True,
                max_execution_time=90,
                handle_parsing_errors="Check your output and make sure it conforms!",
                callbacks=[CustomCallbackHandler()],
            )

            steps = []
            for s in agent_executor.iter(
                {"input": human_prompt, "history": history.messages}
            ):
                yield dumps(s)
                tmp = json.loads(dumps(s))
                if "output" in tmp.keys():
                    print()
                    print("final output", s)
                    print()

                    history.add_user_message(human_prompt)

                    final_steps = []
                    for s in steps:
                        final_steps.append(
                            {
                                "tool": pydash.get(s, "0.0.tool"),
                                "tool_input": pydash.get(s, "0.0.tool_input"),
                            }
                        )
                    toc = time.perf_counter()
                    dt = datetime.now(timezone.utc)
                    save_agent_stats(tic, toc, dt, final_steps)
                else:
                    steps.append(s["intermediate_step"])

        except Exception as e:
            print("*- ERROR -*")
            print(e)
            yield dumps({"error": e})

    return Response(stream_with_context(generate()), mimetype="text/plain")
