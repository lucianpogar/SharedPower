import sqlite3
from sqlite3 import Error

class DatabaseHelpers :

    @staticmethod
    def createConnection() :

        function_name = 'createConnection'

        try:
            database_connection = sqlite3.connect('C:\\Users\\marci\\OneDrive\\Pulpit\\SharedPower\\data\database.db')

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