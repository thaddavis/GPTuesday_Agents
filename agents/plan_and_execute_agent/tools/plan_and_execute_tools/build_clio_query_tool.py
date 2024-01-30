from langchain.agents import Tool
from langchain.tools import StructuredTool

from agents.plan_and_execute_agent.tool_functions.build_clio_query import (
    build_clio_query,
)

BuildClioQueryTool = StructuredTool.from_function(
    name="BuildClioQueryTool",
    func=build_clio_query,
    description="This tool is used to generate a valid SQL command that answers the natural language prompt specified as the input. This tool will reference the database schema for the Clio database and use it to generate an SQL command that can be passed to the 'RunClioQueryTool' tool to execute it. Clio is a popular legal case management software. All names are stored in lowercase in the Clio database. Use flexible search techniques when generating the SQL to grab as much data as possible from the database that is relevant to the prompt. This tool should be used along with the 'RunClioQueryTool' tool to return the SQL results of the query. Never return SQL directly to the prompter.",
)
