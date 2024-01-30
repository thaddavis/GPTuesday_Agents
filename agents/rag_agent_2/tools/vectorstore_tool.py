from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.agents.agent_toolkits import create_retriever_tool

embeddings = OpenAIEmbeddings()
docsearch = Pinecone.from_existing_index("gptuesday-kb", embeddings)
retriever = docsearch.as_retriever()
VectorStoreTool = create_retriever_tool(
    retriever,
    "gptuesday-kb",
    "Searches and returns knowledge related to GPTuesday.",
)
