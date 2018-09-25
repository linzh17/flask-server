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
        return '<User %r>' % self.nickName