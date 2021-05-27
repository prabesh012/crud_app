from flask import render_template, jsonify
from paper_management import app
from paper_management.models import Paper   

@app.route("/")
def index():
    papers = Paper.query.all()
    return render_template("index.html",papers=papers)

# @app.route("/search")
# def search():
#     papers = Paper.query.
#     return jsonify(papers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html"), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template("403error.html"), 403

if __name__ == "__main__":
    app.run(debug=True)