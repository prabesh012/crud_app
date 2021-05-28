from flask import Blueprint, redirect, render_template, url_for, abort, flash,request, send_file
from flask_login import current_user,login_required
from paper_management import db,app,mail
from paper_management.models import Paper, User
from paper_management.papers.forms import AddForm, DelForm, UpdateForm
from werkzeug.utils import secure_filename
from flask_mail import Message
import os
papers_blueprints = Blueprint('papers',__name__,template_folder='templates/papers')

# CREATE
@papers_blueprints.route('/addpaper',methods=['GET','POST'])
@login_required
def addpaper():
    form = AddForm()
    if form.validate_on_submit():
        research_pdf =  request.files['research_file']
        filename = secure_filename(research_pdf.filename)
        file_location = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        research_pdf.save(file_location)
        paper = Paper(title=form.title.data,
                    author=form.author.data,
                    publish_date=form.publish_date.data,
                    category=form.category.data,
                    research_file=file_location,
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
        research_pdf =  request.files['research_file']
        filename = secure_filename(research_pdf.filename)
        file_location = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        research_pdf.save(file_location)
        paper.title = form.title.data
        paper.author = form.author.data
        paper.publish_date = form.publish_date.data
        paper.category = form.category.data
        paper.research_file = file_location
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

@papers_blueprints.route('/download/<int:id>',methods=['GET'])
@login_required
def download(id):
    paper = Paper.query.get_or_404(id)
    user_id  = paper.user_id
    user = User.query.get_or_404(user_id)
    user_email = user.email
    file_name = paper.research_file.split("/")
    message = Message("Here is your file",recipients=[user_email])
    with app.open_resource(paper.research_file) as pdf:
        message.attach(file_name[-1], "application/pdf", pdf.read())
        mail.send(message)
        flash("Check your mail")
    return redirect(url_for('index'))
    # return send_file(paper.research_file, as_attachment=True,download_name=file_name[-1])
