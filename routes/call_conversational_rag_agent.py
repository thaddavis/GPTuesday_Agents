from typing import List
from flask import Blueprint, request
from langchain.tools import BaseTool
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI

loader = TextLoader("./scratch/kb.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()
tool = create_retriever_tool(
    retriever,
    "kb",
    "Searches and returns related knowledge.",
)
tools: List[BaseTool] = [tool]

llm = ChatOpenAI(temperature=0)

agent_executor = create_conversational_retrieval_agent(
    llm, tools, verbose=True, max_token_limit=4000
)

call_conversational_rag_agent_blueprint = Blueprint(
    "call_conversational_rag_agent", __name__
)


@call_conversational_rag_agent_blueprint.route(
    "/call_conversational_rag_agent", methods=["POST"]
)
def call_conversational_rag_agent():
    print("call_conversational_rag_agent")
    content_type = request.headers.get("Content-Type")
    prompt = None
    if content_type == "application/json" and request.json:
        json_payload = request.json
        prompt = json_payload["prompt"]
    else:
        return "Content-Type not supported!"

    result = agent_executor({"input": prompt})

    return {"tool": "RAG_AGENT", "completion": result["output"]}
