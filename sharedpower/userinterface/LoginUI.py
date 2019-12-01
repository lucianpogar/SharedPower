from ..controllers.UserController import UserController

class LoginUI :
    def run(self) :
        print('Enter your credentials')
        username = input('Username: \n')
        password = input('Password: \n')
        user_controller = UserController()
        credentials = {
            'username' : username,
            'password' : password
        }
        print(user_controller.authorise(credentials))
        