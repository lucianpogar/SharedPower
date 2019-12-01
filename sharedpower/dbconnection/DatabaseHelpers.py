import sqlite3
from sqlite3 import Error
import os

class DatabaseHelpers :

    @staticmethod
    def createConnection() :

        file_path = os.path.abspath('./data/database.db')
        function_name = 'createConnection'

        try:
            
            database_connection = sqlite3.connect(file_path)

        except Error as e:
            print(__name__, ':', function_name, ':', e)
            raise

        return database_connection

    @staticmethod
    def closeConnection(database_connection) :
        function_name = 'closeConnection'

        try:
            database_connection.close()

        except Error as e:
            print(__name__, ':', function_name, ':', e)
            raise