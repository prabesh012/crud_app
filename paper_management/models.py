from enum import unique
from operator import index
from paper_management import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    publish_date = db.Column(db.Date)
    category = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id',ondelete='CASCADE'),nullable=False)

    def __init__(self,title,author,publish_date,category,user_id):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category
        self.user_id = user_id

    def __repr__(self):
        return f"Paper {self.title} was created by {self.author} on {self.publish_date}"
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique = True, index=True)
    username = db.Column(db.String(64),unique= True, index=True)
    password_hash = db.Column(db.String(128))
    papers = db.relationship('Paper',backref='user',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash  = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
