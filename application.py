from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date, datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    publish_date = db.Column(db.Date)
    category = db.Column(db.Text)
    # upload_by = User

    def __init__(self,title,author,publish_date,category):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category

    def __repr__(self):
        return f"Paper {self.title} was created by {self.author} on {self.publish_date}"

def setup():
    db.create_all()
setup()

@app.route("/")
def index():
    papers = Paper.query.all()
    return render_template("index.html",papers=papers)

@app.route("/addpaper")
def addpaper():
    return render_template("addpaper.html")
        
# @app.route("/search")
# def search():

@app.route("/create")
def create():
    title = request.args.get("title")
    author = request.args.get("author")
    publish_date = request.args.get("publish_date")
    publish_date = datetime.strptime(publish_date,"%Y-%m-%d").date()
    category = request.args.get("category")
    paper = Paper(title,author,publish_date,category)
    db.session.add(paper)
    db.session.commit()
    return redirect("/")

# @app.route("/update")
# def update():
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html"), 404

if __name__ == "__main__":
    app.run(debug=True)