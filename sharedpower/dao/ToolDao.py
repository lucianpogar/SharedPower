from ..dbconnection.DatabaseHelpers import DatabaseHelpers

class ToolDao:
    def findByName(self, tool_name):
        database_connection = DatabaseHelpers.createConnection()
        cursor = database_connection.cursor()
        cursor.execute('SELECT tool_name, is_active, price_per_day, price_per_half_day, fine FROM TOOL WHERE tool_name = ?', (tool_name,))
        tool_row = cursor.fetchall()
        for i in tool_row:
            print(i)
        DatabaseHelpers.closeConnection(database_connection)
        return tool_row