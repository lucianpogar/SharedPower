from sharedpower.userinterface.LoginUI import LoginUI
from sharedpower.userinterface.PostToolsUI import PostToolsUI
from sharedpower.userinterface.SearchToolsUI import SearchToolsUI
from sharedpower.userinterface.ReturnToolsUI import ReturnToolsUI
from sharedpower.userinterface.CreateAccountUI import CreateAccountUI

class MenuUI :
    def __init__(self) :
        self.login = LoginUI()
        self.post_tools = PostToolsUI()
        self.search_tools = SearchToolsUI()
        self.return_tools = ReturnToolsUI()
        self.create_account = CreateAccountUI()

    def beforeLogin(self) :
        options = 'Choose your option:\n'
        options += '1. Login\n'
        options += '2. Create an account\n\n'

        print('\nHi! Welcome to Shared Power\n')
        choice = input(options)
        self.switchLogin(choice)

    def afterLogin(self) :
        options = 'Choose your option:\n'
        options += '1. Post tools\n'
        options += '2. Search tools\n'
        options += '3. Return tools\n'

        print('\nHi! Welcome to Shared Power\n')
        choice = input(options)
        self.switchLoggedin(choice)

    def switchLoggedin(self, x) :
        switcher = {
            '1' : self.login.run,
            '2' : self.post_tools.run,
            '3' : self.search_tools.run,
            '4' : self.return_tools.run,
            '5' : self.create_account.run
        }
        return switcher.get(x)()

    def switchLogin(self, x) :
        switcher = {
            '1' : self.login.run,
            '2' : self.create_account.run
        }
        return switcher.get(x)()