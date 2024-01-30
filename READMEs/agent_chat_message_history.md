# Tips for setting up long term memory

## PostgresChatMessageHistory
- STEP 0 - Connect to postgres server
`docker run -it --rm --network bridge postgres psql -h 172.17.0.4 -U postgres`
- STEP 1 - Create a database for storing `chat_history` messages
```.sql
CREATE DATABASE chat_history;
```
- STEP 2
```.py Pseudocode
from langchain.memory import PostgresChatMessageHistory

history = None
try:
    history = PostgresChatMessageHistory(
        connection_string=os.getenv(
            "CHAT_MESSAGE_HISTORY_DB_CONNECTION_STRING"
        )
        or "ERROR",
        session_id="test",
    )
except BaseException:
    history = ChatMessageHistory()
memory_key = "history"
memory = AgentTokenBufferMemory(
    memory_key=memory_key, llm=llm, chat_memory=history
)
```

### Reference links
https://python.langchain.com/docs/integrations/memory/postgres_chat_message_history

## VectorStoreRetrieverMemory
Suggested design is to make a retriever tool for selectively storing messages in a "long-term" memory bank

### Reference links
https://python.langchain.com/docs/modules/memory/types/vectorstore_retriever_memory