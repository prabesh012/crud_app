from flask import Flask, render_template, request
from __main__ import app, users_list

@app.route('/users/', methods=['GET', 'POST'])
def disp_users():
   return render_template('/users.html', show = users_list)

@app.route('/users/added',methods=['GET', 'POST'])
def users_added():
   if (request.form['Submit Button'] == 'Add'):
        name = request.form['name']
        if(name != ""):
            users_list.append({'name':name, 'Papers Submitted':'0', 'Papers Downloaded':'0'})
   return render_template('/users.html', show = users_list)

@app.route('/users/add-user/', methods=['GET', 'POST'])
def add_users():
   return render_template('/add_user.html')