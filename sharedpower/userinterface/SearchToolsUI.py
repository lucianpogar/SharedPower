from ..controllers.ToolController import ToolController
#from ..model.Specification import toolSpecification

class SearchToolsUI :
    def run(self) :
        tool_name = input("Type the name of the tool you are looking for: ")
        print("The information below contain: tool name, is it available?, price per day, price per half day, fine.")
        tool_controller = ToolController()
        tool_controller.findByName(tool_name)

        
    