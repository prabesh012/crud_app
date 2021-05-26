from flask import render_template
from paper_management import app
from paper_management.models import Paper   

# def setup():
#     db.create_all()
# setup()

@app.route("/")
def index():
    papers = Paper.query.all()
    return render_template("index.html",papers=papers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404error.html"), 404

if __name__ == "__main__":
    app.run(debug=True)