# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Pinecone
# from langchain.agents.agent_toolkits import create_retriever_tool

# embeddings = OpenAIEmbeddings()
# docsearch = Pinecone.from_existing_index("official-kb", embeddings)
# retriever = docsearch.as_retriever()
# VectorStoreTool = create_retriever_tool(
#     retriever,
#     "official-kb",
#     "Searches and returns related knowledge.",
# )
