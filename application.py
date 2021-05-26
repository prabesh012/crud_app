from forms import AddForm, DelForm, UpdateForm
from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
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

@app.route("/addpaper",methods=['GET','POST'])
def addpaper():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        publish_date = form.publish_date.data
        category = form.category.data
        form.category.data=''
        form.publish_date.data=''
        form.author.data=''
        form.title.data=''
        paper = Paper(title,author,publish_date,category)
        db.session.add(paper)   
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("addpaper.html",form=form)

@app.route('/papers/<int:id>',methods=["GET"])
def papers(id):
    paper = Paper.query.get(id)
    return render_template("paper.html",paper=paper)


# @app.route("/search")
# def search():

@app.route("/update/<int:id>",methods=['GET','POST'])
def update(id):
    form = UpdateForm()
    form.id = id
    paper = Paper.query.get_or_404(id)
    print(paper)
    if form.validate_on_submit():
        paper.title = form.title.data
        paper.author = form.author.data
        paper.publish_date = form.publish_date.data
        paper.category = form.category.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html',form=form,paper=paper)

    
@app.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    form = DelForm()
    form.id = id
    paper = Paper.query.get(id)
    if form.validate_on_submit():
        db.session.delete(paper)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html',form=form,paper=paper)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html"), 404

if __name__ == "__main__":
    app.run(debug=True)