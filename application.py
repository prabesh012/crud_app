from flask import render_template, request,flash,redirect
from paper_management import app
from paper_management.models import Paper   

@app.route("/")
def index():
    papers = Paper.query.all()
    return render_template("index.html",papers=papers)

@app.route("/search")
def search():
    search_title = request.args.get("query")
    sql_search_title = '%'+search_title+'%'
    papers = Paper.query.filter(Paper.title.like(sql_search_title)).all()
    return render_template('search.html',papers=papers,search_term=search_title)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html"), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template("403error.html"), 403

if __name__ == "__main__":
    app.run(debug=True)