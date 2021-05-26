from paper_management import db

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    publish_date = db.Column(db.Date)
    category = db.Column(db.Text)
    # upload_by = User

    def __init__(self,title,author,publish_date,category):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category

    def __repr__(self):
        return f"Paper {self.title} was created by {self.author} on {self.publish_date}"