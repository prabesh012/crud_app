from flask import Blueprint, redirect, render_template, url_for, abort, flash
from flask_login import current_user,login_required
from paper_management import db
from paper_management.models import Paper
from paper_management.papers.forms import AddForm, DelForm, UpdateForm

papers_blueprints = Blueprint('papers',__name__,template_folder='templates/papers')

# CREATE
@papers_blueprints.route('/addpaper',methods=['GET','POST'])
@login_required
def addpaper():
    form = AddForm()
    if form.validate_on_submit():
        paper = Paper(title=form.title.data,
                    author=form.author.data,
                    publish_date=form.publish_date.data,
                    category=form.category.data,
                    user_id=current_user.id)
        db.session.add(paper)   
        db.session.commit()
        flash('Paper Created!')
        return redirect(url_for('index'))
    return render_template("addpaper.html",form=form)

# READ
@papers_blueprints.route('/papers/<int:id>',methods=['GET'])
def papers(id):
    paper = Paper.query.get_or_404(id)
    return render_template("paper.html",paper=paper)

# UPDATE
@papers_blueprints.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def update(id):
    form = UpdateForm()
    form.id = id
    paper = Paper.query.get_or_404(id)
    if paper.user_id != current_user.id:
        abort(403)
    if form.validate_on_submit():
        paper.title = form.title.data
        paper.author = form.author.data
        paper.publish_date = form.publish_date.data
        paper.category = form.category.data
        db.session.commit()
        flash('Paper Updated!')
        return redirect(url_for('index'))
    return render_template('update.html',form=form,paper=paper)
    
# DELETE
@papers_blueprints.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
    form = DelForm()
    form.id = id
    paper = Paper.query.get_or_404(id)
    if paper.user_id != current_user.id:
        abort(403)
    if form.validate_on_submit():
        db.session.delete(paper)
        db.session.commit()
        flash('Paper Deleted!')
        return redirect(url_for('index'))
    return render_template('delete.html',form=form,paper=paper)