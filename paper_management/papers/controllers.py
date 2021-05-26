from flask import Blueprint, redirect, render_template, url_for
from paper_management import db
from paper_management.models import Paper
from paper_management.papers.forms import AddForm, DelForm, UpdateForm

papers_blueprints = Blueprint('papers',__name__,template_folder='templates/papers')

# @app.route("/addpaper",methods=['GET','POST'])
@papers_blueprints.route('/addpaper',methods=['GET','POST'])
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

# @app.route('/papers/<int:id>',methods=["GET"])
@papers_blueprints.route('/papers/<int:id>',methods=['GET'])
def papers(id):
    paper = Paper.query.get(id)
    return render_template("paper.html",paper=paper)

# @app.route("/update/<int:id>",methods=['GET','POST'])
@papers_blueprints.route('/update/<int:id>',methods=['GET','POST'])
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
    
# @app.route("/delete/<int:id>",methods=['GET','POST'])
@papers_blueprints.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    form = DelForm()
    form.id = id
    paper = Paper.query.get(id)
    if form.validate_on_submit():
        db.session.delete(paper)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html',form=form,paper=paper)