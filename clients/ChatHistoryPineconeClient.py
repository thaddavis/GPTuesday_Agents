import pinecone
import os
import logging


class ChatHistoryPineconeClient:
    pineconeInstance = None

    @staticmethod
    def connectPinecone():
        try:
            # initialize pinecone
            ChatHistoryPineconeClient.pineconeInstance = pinecone.init(
                api_key=os.getenv("CHAT_HISTORY_PINECONE_API_KEY") or "ERROR",
                environment=os.getenv("CHAT_HISTORY_PINECONE_ENV") or "ERROR",
            )
        except BaseException as e:
            logging.exception("An exception was thrown!")
            print("Exception", e)
        # finally:
        #     print('Finally', err)

    @staticmethod
    def setPineconeDb():
        ChatHistoryPineconeClient.connectPinecone()

    @staticmethod
    def getPineconeDb():
        if ChatHistoryPineconeClient.pineconeInstance:
            return ChatHistoryPineconeClient.pineconeInstance
        else:
            ChatHistoryPineconeClient.pineconeInstance
            return ChatHistoryPineconeClient.pineconeInstance
