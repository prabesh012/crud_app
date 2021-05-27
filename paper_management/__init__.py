import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
login_manager.init_app(app)
login_manager.login_view = 'login'

from paper_management.papers.controllers import papers_blueprints
app.register_blueprint(papers_blueprints,url_prefix='/papers')

from paper_management.users.controller import users_blueprints
app.register_blueprint(users_blueprints,url_prefix='/users')