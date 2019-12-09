from ..dbconnection.DatabaseHelpers import DatabaseHelpers

class ToolDao:
    def findByName(self, toolName):
        #connecting to the database
        database_connection = DatabaseHelpers.createConnection()

        #creating a cursor that will allow SQL commands to be executed in python
        cursor = database_connection.cursor()

        #creating a query that the cursor can follow in order to retrieve data
        cursor.execute('SELECT tool_name, is_active, price_per_day, price_per_half_day, fine FROM TOOL WHERE tool_name = ?')

        #retrieving one or more records from the database
        tool_row = cursor.fetchall()

        #disconnecting from the database
        DatabaseHelpers.closeConnection(database_connection)

        #displaying all the records that are adequate to the tool's name
        return tool_row