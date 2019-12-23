from ..controllers.ToolController import ToolController
#from ..model.Specification import toolSpecification

class SearchToolsUI :
    def caseStatement(self, chosen_item):
        switcher = {
            "1" : "pass",
            "2" : "pass",
        }
        print(switcher.get(chosen_item))
    
    def run(self) :
        tool_name = input("Type the name of the tool you are looking for: ")
        print("The information below contain: tool name, is it available?, price per day, price per half day, fine.")
        tool_controller = ToolController()
        tool_controller.findByName(tool_name)
        chosen_item = input("Choose the item of your interest by typing a number: ")
        self.caseStatement(chosen_item)
        
    