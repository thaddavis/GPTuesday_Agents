from flask import Blueprint, request
from langchain.agents import Tool

# from agents.tools.build_query import build_query
# from agents.tools.run_query import run_query
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents.output_parsers import JSONAgentOutputParser
from langchain.agents.format_scratchpad import format_log_to_messages
from time import sleep
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from pydash import get

# from agent.tools.build_query import build_query
# from agent.tools.run_query import run_query

call_hwchase17_conversational_agent_blueprint = Blueprint(
    "call_hwchase17_conversational_agent", __name__
)


@call_hwchase17_conversational_agent_blueprint.route(
    "/call_hwchase17_conversational_agent", methods=["POST"]
)
def call_hwchase17_conversational_agent():
    print("call_hwchase17_conversational_agent")
    content_type = request.headers.get("Content-Type")
    prompt = None
    if content_type == "application/json" and request.json:
        json_payload = request.json
        prompt = json_payload["prompt"]
    else:
        return {"content": "Content-Type not supported!"}

    tools = [
        # Tool(
        #     name="BuildClioQuery",
        #     func=build_clio_query,
        #     description="This tool is used to generate a valid SQL command that answers the natural language prompt specified as the input. This tool will reference the database schema for the Clio database and use it to generate the SQL command which can be passed to the `run-clio-query` tool to execute it. Clio is a popular legal case management software. All names are stored in lowercase in the Clio database.",
        # ),
        # Tool(
        #     name="RunClioQuery",
        #     func=run_clio_query,
        #     description="Accepts a valid SQL query and executes it in order to extract information from the Clio database. Clio is a popular legal case management software.",
        # ),
    ]

    prompt = hub.pull("hwchase17/react-chat-json")
    chat_model = ChatOpenAI(temperature=0, model="gpt-4")

    prompt = prompt.partial(
        tools=[],
        tool_names="",
    )

    chat_model_with_stop = chat_model.bind(stop=["\nObservation"])

    TEMPLATE_TOOL_RESPONSE = """TOOL RESPONSE: 
---------------------
{observation}

USER'S INPUT
--------------------

Okay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else - even if you just want to respond to the user. Do NOT respond with anything except a JSON snippet no matter what!"""

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_messages(
                x["intermediate_steps"], template_tool_response=TEMPLATE_TOOL_RESPONSE
            ),
            "chat_history": lambda x: x["chat_history"],
        }
        | prompt
        | chat_model_with_stop
        | JSONAgentOutputParser()
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, memory=memory
    )

    output = agent_executor.invoke({"input": prompt})["output"]

    return {"tool": "AGENT", "completion": output}
