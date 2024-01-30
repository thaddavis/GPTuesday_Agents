"""Callback Handler that prints to std out."""
from typing import Any, Callable, Dict, List, Optional
import sys
from langchain.callbacks.base import BaseCallbackHandler, Callbacks
from langchain.schema import AgentAction, AgentFinish, LLMResult
from langchain.utils.input import print_text

import asyncio


class PlanAndExecuteCallbackHandler(BaseCallbackHandler):
    def __init__(self) -> None:
        super().__init__()

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        print("!((* on_llm_start *))!")
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        print("!((* on_llm_end *))!")
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        print("!((* on_llm_new_token *))!")
        pass

    def on_llm_error(self, error: BaseException, **kwargs: Any) -> None:
        # print("!((* on_llm_error *))!")
        pass

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ):
        print("!((* on_chain_start *))!")
        pass

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        print("!((* on_chain_end *))!")
        pass

    def on_chain_error(self, error: BaseException, **kwargs: Any) -> None:
        # print("!((* on_chain_error *))!")
        pass

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        **kwargs: Any,
    ) -> None:
        print("!((* on_tool_start *))!")
        pass

    def on_agent_action(
        self, action: AgentAction, color: Optional[str] = None, **kwargs: Any
    ) -> Any:
        print("!((* on_agent_action *))!")
        # print(action)
        pass

    def on_tool_end(
        self,
        output: str,
        color: Optional[str] = None,
        observation_prefix: Optional[str] = None,
        llm_prefix: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        print("!((* on_tool_end *))!")
        pass

    def on_tool_error(self, error: BaseException, **kwargs: Any) -> None:
        print("!((* on_tool_error *))!")
        pass

    def on_text(
        self,
        text: str,
        color: Optional[str] = None,
        end: str = "",
        **kwargs: Any,
    ) -> None:
        # print("!((* on_text *))!")
        pass

    def on_agent_finish(
        self, finish: AgentFinish, color: Optional[str] = None, **kwargs: Any
    ) -> None:
        print("!((* on_agent_finish *))!")
        pass
