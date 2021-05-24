from app import app

from flask import render_template, request, redirect

import sqlite3

@app.route('/')
def select_all_tasks():

    conn = sqlite3.connect('fuse.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM fields")
    datas = c.fetchall()


    print(datas)
    print(type(datas))
    mydata = []
    for data in datas:
        mydata.append(data)
    conn.close()
    
   
    # return(l)
    return render_template("papers.html",datas=mydata)




def index():
    return render_template('papers.html')