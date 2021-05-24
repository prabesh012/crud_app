from app import app

from flask import render_template, request, redirect

import sqlite3


@app.route('/')
def select_all_tasks():
    conn = sqlite3.connect('fuse.db')

    c = conn.cursor()

    # c.execute("INSERT INTO papers('title','author','published_on','uploaded_by', 'field' , 'file') VALUES ('Web Development', 'author', '2020-10-02', 'new', 'Macjine' , 'jdv')")

    
    # print(c.fetchall())

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())

    # c = conn.cursor()

    return(c.fetchall())

    # a = c.execute("SELECT * FROM fields")
    # return 'fhdsjkg'
    # c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # return(c.fetchall())

    # rows = c.fetchall()

    # return rows



def index():
    return render_template('papers.html')