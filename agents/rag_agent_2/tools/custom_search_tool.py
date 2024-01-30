from typing import Optional, Type

from langchain.tools import BaseTool, StructuredTool, Tool, tool

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"
    generator: str = ""

    def __init__(self, name, description, generator: str):
        super().__init__(name=name, description=description)
        self.generator = generator

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        print(self.generator)
        return "Search the interwebs"
        # return search.run(query)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
