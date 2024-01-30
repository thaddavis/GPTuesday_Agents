import pinecone
import os
import logging


class PineconeClient:
    pineconeInstance = None

    @staticmethod
    def connectPinecone():
        try:
            # initialize pinecone
            PineconeClient.pineconeInstance = pinecone.init(
                api_key=os.getenv("PINECONE_API_KEY") or "ERROR",
                environment=os.getenv("PINECONE_ENV") or "ERROR",
            )
        except BaseException as e:
            logging.exception("An exception was thrown!")
            print("Exception", e)
        # finally:
        #     print('Finally', err)

    @staticmethod
    def setPineconeDb():
        PineconeClient.connectPinecone()

    @staticmethod
    def getPineconeDb():
        if PineconeClient.pineconeInstance:
            return PineconeClient.pineconeInstance
        else:
            PineconeClient.pineconeInstance
            return PineconeClient.pineconeInstance
