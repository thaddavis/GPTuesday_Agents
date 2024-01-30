from langchain.agents import Tool
from langchain.tools import StructuredTool

from agents.rag_agent_2.tool_functions.run_query import run_query

RunClioQueryTool = StructuredTool.from_function(
    name="RunQueryTool",
    func=run_query,
    description="Accepts a valid SQL query and executes it in order to extract information from a database.",
)
