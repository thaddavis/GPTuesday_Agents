import psycopg2
from psycopg2.extras import RealDictCursor
import logging
import os

DB_PARAMS = {
    # 'database': "clio",
    # 'user': "postgres",
    # 'password': "mysecretpassword",
    # 'host': "127.0.0.1",
    # 'port': 6543,
    "database": os.getenv("DATABASE_NAME"),
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "port": os.getenv("DATABASE_PORT"),
    "cursor_factory": RealDictCursor,
}


class ClioDbClient:
    clioDbInstance = None

    @staticmethod
    def connectClioDb():
        err = None
        try:
            conn = psycopg2.connect(**DB_PARAMS)  # type: ignore
            ClioDbClient.clioDbInstance = conn
        except BaseException as e:
            logging.exception("An exception was thrown!")
            print("Exception", e)
        # finally:
        #     print('Finally', err)

    @staticmethod
    def setClioDb():
        ClioDbClient.connectClioDb()

    @staticmethod
    def getClioDb():
        if ClioDbClient.clioDbInstance:
            return ClioDbClient.clioDbInstance
        else:
            ClioDbClient.connectClioDb()
            return ClioDbClient.clioDbInstance
