from flask import Flask, render_template, request
from __main__ import app, papers_list

@app.route('/papers/', methods=['GET', 'POST'])
def disp_papers():
   return render_template('/papers.html', show = papers_list)

@app.route('/request-paper/', methods=['GET', 'POST'])
def request_paper():
    if (request.form['Submit Button'] == 'Request'):
        return render_template('/request_paper.html', add = 'False')
    elif(request.form['Submit Button'] == 'Add'):
        return render_template('/request_paper.html', add = 'True')
    

@app.route('/papers/requested', methods=['GET', 'POST'])
def paper_requested():
    if (request.form['Submit Button'] == 'Submit'):
        title = request.form['title']
        author = request.form['author']
        if(title != ""):
            if('file' in request.form):
                papers_list.append({'Paper Title':title, 'author':author,'citations':'N/A', 'available':'True'})
            else:
                papers_list.append({'Paper Title':title, 'author':author,'citations':'N/A', 'available':'False'})
    return render_template('/papers.html', show = papers_list)