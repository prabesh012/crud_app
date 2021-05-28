import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))

directory_media = 'media'
media_path = os.path.join(basedir,directory_media)
if not os.path.isdir(media_path):
    os.mkdir(media_path)

directory_uploads = 'uploads'
upload_path = os.path.join(media_path,directory_uploads)
if not os.path.isdir(upload_path):
    os.mkdir(upload_path)


UPLOAD_FOLDER = os.path.join(basedir,'media/uploads')

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

configurations = dotenv_values(".env")
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_DEFAULT_SENDER"] = configurations['MAIL_USERNAME']
app.config["MAIL_USERNAME"] = configurations['MAIL_USERNAME']
app.config["MAIL_PASSWORD"] = configurations['MAIL_PASSWORD']
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

db = SQLAlchemy(app)
Migrate(app,db)
mail = Mail(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from paper_management.papers.controllers import papers_blueprints
app.register_blueprint(papers_blueprints,url_prefix='/papers')

from paper_management.users.controller import users_blueprints
app.register_blueprint(users_blueprints,url_prefix='/users')
