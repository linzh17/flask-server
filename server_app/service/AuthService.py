from server_app import db
from ..model.User_M import LocalUser,User

class authService:
    
    def userRegister(self,username,password):
        user=User(email=username)
        db.session.add(user)
        db.session.commit()
        localuser=LocalUser(email=username,password=password,Userid=user.Userid)
        db.session.add(localuser)
        db.session.commit()

    def localToken(self):
        pass

    def localVerifyToken(self):
        pass 

