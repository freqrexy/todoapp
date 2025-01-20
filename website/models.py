from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete = db.Column(db.Boolean, default = False)
    deadlinetrue = db.Column(db.Boolean, default = False)
    deadline = db.Column(db.String(20), unique = False)
    date = db.Column(db.String(20), unique = False)