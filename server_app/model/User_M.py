from server_app import db

class User(db.Model):

    __tablename__ = 'users'
    Userid = db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64))
    nickName=db.Column(db.String(64))
    city=db.Column(db.String(64))
    country=db.Column(db.String(64))
    avatarUrl=db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.email

    def to_json(self):
        userJson={
            "email":self.email,
            "nickName":self.nickName,
            "city":self.city,
            "country":self.country,
            "avatarUrl":self.avatarUrl,
        }
        return userJson    

class LocalUser(db.Model):
    __tablename__ = 'localusers'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True)
    password=db.Column(db.String(64))

    Userid=db.Column(db.Integer,db.ForeignKey('users.Userid'))


    def to_json(self):
        localuserJson={
            "email":self.email,
            "password":self.password,
        }
        return localuserJson

    def __repr__(self):
        return '<LocalUser %r>' % self.email    
