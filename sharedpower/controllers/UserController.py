from ..daoservice.UserService import UserService

class UserController :
    def authorise(self, data) :
        user_service = UserService()
        return user_service.authorise(data)