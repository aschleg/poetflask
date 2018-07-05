from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.VARCHAR(255), index=True, unique=True)


class Poems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.VARCHAR(255))
    linecount = db.Column(db.Integer)
    lines = db.Column(db.Text, unique=True)
    title = db.Column(db.Text, unique=True)
