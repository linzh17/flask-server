from server_app import db
from ..model.User_M import LocalUser

class authService:
    
    def userRegister(self,username,password):
        user=LocalUser(email=username,password=password)
        db.session.add(user)
        db.session.commit()
