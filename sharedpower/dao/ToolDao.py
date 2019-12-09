from ..dbconnection.DatabaseHelpers import DatabaseHelpers

class ToolDao:
    def findByName(self, name):
        database_connection = DatabaseHelpers.CreateConnection()


        
        DatabaseHelpers.CloseConnection(database_connection)











        #query = 'SELECT username, password FROM USER WHERE username = ?'
        #database_connection = DatabaseHelpers.createConnection()
        #cursor = database_connection.cursor()
        #cursor.execute(query, (username,))
        #customer_row = cursor.fetchone()
        #DatabaseHelpers.closeConnection(database_connection)
        #return customer_row