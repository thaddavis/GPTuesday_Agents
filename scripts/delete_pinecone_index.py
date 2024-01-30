import pinecone
import os
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone


def delete_pinecone_index():
    print("delete_pinecone_index")
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY") or "",  # find at app.pinecone.io
        environment=os.getenv("PINECONE_ENV") or "",  # next to api key in console
    )

    index_name = "kb"
    pinecone.delete_index(index_name)
