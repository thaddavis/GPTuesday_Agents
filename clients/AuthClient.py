import logging
import os


class AuthClient:
    authDbInstance = None

    @staticmethod
    def connectAuthDb():
        err = None
        try:
            AuthClient.authDbInstance = None
        except BaseException as e:
            logging.exception("An exception was thrown!")
            print("Exception", e)
        # finally:
        #     print('Finally', err)

    @staticmethod
    def setClioDb():
        AuthClient.connectAuthDb()

    @staticmethod
    def getClioDb():
        if AuthClient.authDbInstance:
            return AuthClient.authDbInstance
        else:
            AuthClient.connectAuthDb()
            return AuthClient.authDbInstance
