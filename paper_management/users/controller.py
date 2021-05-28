from paper_management import app,db
from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, login_required, logout_user
from paper_management.models import User
from paper_management.users.forms import LoginForm, RegistrationForm

users_blueprints = Blueprint('users',__name__,template_folder='templates/users')

# LOGOUT
@users_blueprints.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out",'success')
    return redirect(url_for('index'))

# LOGIN
@users_blueprints.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in Successfully!!!",'success')

            next = request.args.get('next')
            if next == None or not next[0] =='/':
                next = url_for('index')
            return redirect(next)
        else:
            flash('Incorrect Information!','danger')
            return redirect(url_for('users.login'))
    return render_template('login.html',form=form)

# REGISTER
@users_blueprints.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("here")
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration','success')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)