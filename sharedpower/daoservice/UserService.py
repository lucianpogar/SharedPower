from ..dao.UserDao import UserDao
from passlib.hash import bcrypt

class UserService :
    def authorise(self, data) :
        userDao = UserDao()
        user_row = userDao.findByUsername(data.get('username'))
        if bcrypt.verify(data.get('password'), user_row[1]) :
            return True
        else :
            return False