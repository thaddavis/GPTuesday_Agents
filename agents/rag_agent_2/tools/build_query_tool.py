from langchain.agents import Tool

from agents.rag_agent_2.tool_functions.build_query import build_query

BuildQueryTool = Tool(
    name="BuildQuery",
    func=build_query,
    description="This tool is used to generate a valid SQL command that answers the natural language prompt specified as the input. This tool will reference the schema for an SQL database and use it to generate an SQL command that will always be passed to the `RunQuery` tool to execute it. All names are stored in lowercase in the database. Use flexible search techniques when generating the SQL to grab as much data as possible from the database that is relevant to the prompt. This tool should always be used with the RunQuery tool to return the SQL results of the query. Never return raw SQL code directly to the prompter.",
)
