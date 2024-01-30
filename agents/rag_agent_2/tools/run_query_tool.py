from langchain.agents import Tool

from agents.rag_agent_2.tool_functions.run_query import run_query

RunQueryTool = Tool(
    name="RunQueryTool",
    func=run_query,
    description="Accepts a valid SQL query and executes it in order to extract information from a database.",
    return_direct=True,
)
