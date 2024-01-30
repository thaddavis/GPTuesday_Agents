import uuid
import pinecone
from pinecone import index
import os
import openai
from langchain.vectorstores import Pinecone

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY") or "",  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV") or "",  # next to api key in console
)


def add_to_pinecone_index():
    # index_name = "quickstart"
    question = "Who is Mukaddas"

    # answer = "Founder of GPTuesday"

    # metadata = {
    #     "question": question,
    #     "answer": answer,
    #     "source": "kb",
    #     "author": "Tad Duval",
    #     "created_at": "1-30-2024",
    #     "text": f"{question}\n{answer}",
    # }
    # index = pinecone.Index(index_name)

    embedding_response = openai.embeddings.create(
        input=question, model="text-embedding-ada-002"
    )
    embedding = embedding_response.data[0].embedding
    print("vector embedding returned:", embedding)

    # index.upsert([(str(uuid.uuid4()), embedding, metadata)])
