from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    category = db.Column(db.String(300), unique = False)
    complete = db.Column(db.Boolean, default = False)
    deadlinetrue = db.Column(db.Boolean, default = False)
    deadline = db.Column(db.String(20), unique = False)
    date = db.Column(db.String(20), unique = False)

    # I added not only the stretch goal of adding a category, but also adding an option for urgency.
    # The variable "deadlinetrue" is a boolean value that can determine the value's urgency.
    # That means if the boolean value is True, "deadline" will have a date inputted as a string.
    # If "deadlinetrue" returns False, then the value for "deadline" will be "None".