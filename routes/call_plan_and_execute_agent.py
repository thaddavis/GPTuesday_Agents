import time
from flask import Blueprint, request, stream_with_context, Response
from basic_auth.index import auth
from langchain.load.dump import dumps
import json
from datetime import datetime, timezone
import pydash
from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain.llms import OpenAI
from langchain.chains.llm_math.base import LLMMathChain
from langchain.tools import BaseTool
from agents.plan_and_execute_agent.callback_handlers.plan_and_execute_callback_handler import (
    PlanAndExecuteCallbackHandler,
)
from agents.plan_and_execute_agent.tools.plan_and_execute_tools import (
    BuildClioQueryTool,
    RunClioQueryTool,
)

llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
tools: list[BaseTool] = [BuildClioQueryTool, RunClioQueryTool]

call_plan_and_execute_agent_blueprint = Blueprint(
    "call_plan_and_execute_agent", __name__
)


@call_plan_and_execute_agent_blueprint.route(
    "/call_plan_and_execute_agent", methods=["POST"]
)
@auth.login_required
def call_plan_and_execute_agent():
    def generate():
        print("entering Plan & Execute Agent generate...")
        try:
            tic = time.perf_counter()
            content_type = request.headers.get("Content-Type")
            human_prompt = None
            if content_type == "application/json" and request.json:
                json_payload = request.json
                human_prompt = json_payload["prompt"]
            else:
                return "Content-Type not supported!"
            print("human_prompt", human_prompt)
            model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
            planner = load_chat_planner(model)
            executor = load_agent_executor(model, tools, verbose=True)
            agent = PlanAndExecute(
                planner=planner,
                executor=executor,
                verbose=True,
                callbacks=[PlanAndExecuteCallbackHandler()],
            )
            # for s in executor._iter({"input": human_prompt}):
            #     yield dumps(s)
            for s in agent.stream({"input": human_prompt}):
                print("-!-!-!-")
                s["step_container"] = agent.step_container
                print(s)
                yield dumps(s)

        except Exception as e:
            print("*- ERROR -*")
            print(e)
            yield dumps({"error": e})

    return Response(stream_with_context(generate()), mimetype="text/plain")
