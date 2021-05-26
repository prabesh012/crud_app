import os
from flask import Flask
import flask


from werkzeug.utils import secure_filename

app = Flask(__name__)

from flask import render_template, request, redirect, send_file

import sqlite3
import time

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    conn = sqlite3.connect('fuse.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM fields")
    datas = c.fetchall()

    mydata = []
    for data in datas:
        mydata.append(data)
        print(data)
    conn.close()
   
    return render_template("papers.html",datas=mydata)


@app.route("/paper", methods=["POST"])
def paper():

     if request.method == "POST": 

        file = request.files['papers']

        # return(request.files['papers'].filename)

        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)

        #Uploading thr file to the system if it is a pdf file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            #Saving data to the database
            field = request.files['papers'].filename            
            dbms = sqlite3.connect('fuse.db')
            db = dbms.cursor()

            db.execute("INSERT INTO fields VALUES (?)",(field,))

            dbms.commit()
            db.close()

        return redirect('/')
        # else:
        #     flash('No selected file')
        #     return redirect('/')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/showfile/<data>")
def showfile(data):
    data_path = (os.path.join(app.config['UPLOAD_FOLDER'], data))
    sliced_path = data_path[2:]

    basedir = os.path.abspath(os.path.dirname(__file__))
    final = 'files:' +os.path.join(basedir,'files', data)

    #to download the file
    return send_file(final, as_attachment=True)

    #to view the file
    # return render_template("showpdf.html",path=final)


if __name__ == '__main__':
    app.run(debug=True)