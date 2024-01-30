import pinecone
import os
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone


def build_pinecone_index():
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY") or "",  # find at app.pinecone.io
        environment=os.getenv("PINECONE_ENV") or "",  # next to api key in console
    )
    embeddings = OpenAIEmbeddings()
    index_name = "kb"

    for i in pinecone.list_indexes():
        print("i", i)

    if index_name not in pinecone.list_indexes():
        # we create a new index
        pinecone.create_index(name=index_name, metric="cosine", dimension=1536)

    loader = TextLoader("./scratch/kb.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
    Pinecone.from_documents(docs, embeddings, index_name=index_name)
    # # if you already have an index, you can load it like this
    # # docsearch = Pinecone.from_existing_index(index_name, embeddings)

    # query = "What did the president say about Ketanji Brown Jackson"
    # docs = docsearch.similarity_search(query)
