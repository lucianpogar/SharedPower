from sharedpower.userinterface.LoginUI import LoginUI
from sharedpower.userinterface.PostToolsUI import PostToolsUI
from sharedpower.userinterface.SearchToolsUI import SearchToolsUI
from sharedpower.userinterface.ReturnToolsUI import ReturnToolsUI
from sharedpower.userinterface.CreateAccountUI import CreateAccountUI

class MenuUI :
    def run(self) :
        options = 'Choose your option:\n'
        options += '1. Login\n'
        options += '2. Post tools\n'
        options += '3. Search tools\n'
        options += '4. Return tools\n'
        options += '5. Create an account\n\n'

        print('\nHi! Welcome to Shared Power\n')
        choice = input(options)
        self.switch(choice)
    

    def switch(self, x) :
        login = LoginUI()
        post_tools = PostToolsUI()
        search_tools = SearchToolsUI()
        return_tools = ReturnToolsUI()
        create_account = CreateAccountUI()
        switcher = {
            '1' : login.run,
            '2' : post_tools.run,
            '3' : search_tools.run,
            '4' : return_tools.run,
            '5' : create_account.run
        }
        return switcher.get(x)()