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


class DbClient:
    dbInstance = None

    @staticmethod
    def connectDb():
        err = None
        try:
            conn = psycopg2.connect(**DB_PARAMS)  # type: ignore
            DbClient.dbInstance = conn
        except BaseException as e:
            logging.exception("An exception was thrown!")
            print("Exception", e)
        # finally:
        #     print('Finally', err)

    @staticmethod
    def setDb():
        DbClient.connectDb()

    @staticmethod
    def getDb():
        if DbClient.dbInstance:
            return DbClient.dbInstance
        else:
            DbClient.connectDb()
            return DbClient.dbInstance
