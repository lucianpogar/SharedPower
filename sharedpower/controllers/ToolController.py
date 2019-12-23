from ..dao.ToolDao import ToolDao 

class ToolController : 
    def findByName(self, tool_name):
        tool_service = ToolDao()
        return tool_service.findByName(tool_name)