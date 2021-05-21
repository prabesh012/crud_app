from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

todo_list = []

@app.route('/todo/', methods=['POST','GET'])
def todo():
   if request.method == 'POST':
      activity = request.form['todo']
      if(activity!=""):
         todo_list.append(activity)
   elif request.method == 'GET':
      activity = request.args.get('todo')
   return render_template('todo.html', show = todo_list)

@app.route('/todo/<int:id>/delete', methods=['POST'])
def delete(id):
   if request.method == 'POST':
      todo_list.pop(id-1)
   return render_template('todo.html', show = todo_list)

@app.route('/todo/<int:id>/update', methods=['POST'])
def update(id):
   if request.method == 'POST':
      return render_template('update.html', list = todo_list, id = id-1)

@app.route('/todo/<int:id>/complete-update', methods=['POST'])
def complete_update(id):
   if request.method == 'POST':
      activity = request.form['todo']
      if(activity!=""):
         todo_list[id] = activity
      return render_template('todo.html', show = todo_list)

if __name__ == '__main__':
   app.run(debug = True)