from flask import Blueprint, request
from langchain.agents import Tool

# from agent.tools.build_clio_query import build_clio_query
# from agent.tools.run_clio_query import run_clio_query
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from time import sleep
from langchain.agents import AgentType, initialize_agent

call_conversational_agent_blueprint = Blueprint("call_conversational_agent", __name__)


@call_conversational_agent_blueprint.route(
    "/call_conversational_agent", methods=["POST"]
)
def call_conversational_agent():
    print("call_conversational_agent")
    content_type = request.headers.get("Content-Type")
    prompt = None
    if content_type == "application/json" and request.json:
        json_payload = request.json
        prompt = json_payload["prompt"]
    else:
        return "Content-Type not supported!"
    tools = [
        # Tool(
        #     name="BuildClioQuery",
        #     func=build_clio_query,
        #     description="This tool is used to generate a valid SQL command that answers the natural language prompt specified as the input. This tool will reference the database schema for the Clio database and use it to generate the SQL command which can be passed to the `run-clio-query` tool to execute it. Clio is a popular legal case management software. All names are stored in lowercase in the Clio database.",
        # ),
        # Tool(
        #     name="RunClioQuery",
        #     func=run_clio_query,
        #     description="Accepts a valid SQL query and executes it in order to extract information from the Clio database. Clio is a popular legal case management software. This tool can take an SQL query generated from the BuildClioQuery tool.",
        # ),
    ]
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
    )
    output = agent.run(prompt)
    return {"tool": "CONVERSATIONAL_AGENT", "completion": output}
