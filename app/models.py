# File for models/classes
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    #
    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    #
    @property
    def password(self):
        raise AttributeError('You Cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ ='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role', lazy = "dynamic")


    def __repr__(self):
        return f'User {self.name}'
