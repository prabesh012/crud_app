from flask import Flask

app = Flask(__name__)

from flask import render_template, request, redirect

import sqlite3

@app.route('/')
def index():

    conn = sqlite3.connect('fuse.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM fields")
    datas = c.fetchall()

    print(datas)
    print(type(datas))
    mydata = []
    for data in datas:
        mydata.append(data)
        print(data)
    conn.close()
    
    print(mydata)
   
    # return(l)
    return render_template("papers.html",datas=mydata)





if __name__ == '__main__':
    app.run(debug=True)