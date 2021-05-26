import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'database.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    publish_date = db.Column(db.Text)
    category = db.Column(db.Text)
    # upload_by = User

    def __init__(self,title,author,publish_date,category):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category

    def __repr__(self):
        return f"Paper {self.title} was created by {self.author} on {self.publish_date}"
        