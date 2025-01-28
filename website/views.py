from flask import Flask, Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db
from datetime import datetime

my_view = Blueprint("my_view",__name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get("message",None)
    return render_template("index.html", todo_list=todo_list, message=message)

# In the below Add route, most variables are taken from the form get funciton on the HTML page.
# The only exception is datetime.today(), which always returns today's date and requires the Datetime library to work.
# Deadlinetrue starts as false, but needs a separate value from the form and an If loop to return the boolean value.

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        category = request.form.get("category")
        today = datetime.today()
        endtrue = request.form.get("deadlinetrue")
        deadlinetrue = False
        if endtrue == "true":
            deadlinetrue = True
        deadline = request.form.get("deadline")
        new_todo = Todo(task=task, category=category, date=today.strftime("%Y-%m-%d"), deadlinetrue=deadlinetrue, deadline=deadline)
        db.session.add(new_todo)
        db.session.commit()
        message = "Task added successfully."
        return redirect(url_for("my_view.home",message=message))
    except:
        message = "There was an error adding your task.  Please try again."
        return redirect(url_for("my_view.home",message=message))

    # One thing I'd like to do with more time is varying up what errors were made user-side, so that I know what to fix.
    # This will require more outside research into error handling proceedings.

@my_view.route("/edit/<todo_id>", methods=["POST"])
def edit(todo_id):
    try:
        edit_todo = request.form.get("edit_todo")
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.task = edit_todo
        db.session.commit()
        message = "Task edited successfully."
        return redirect(url_for("my_view.home",message=message))
    except:
        message = "There was an error editing your task.  Please try again."
        return redirect(url_for("my_view.home",message=message))

        # As of right now, there is a function to edit the wording of a task.  More could be done with more time.
        # Same story as before with error handling and advanced functions.

@my_view.route("/update/<todo_id>", methods=["POST"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    if todo.complete == True:
        message = "Task complete"
    else:
        message = "Completion undone"
    return redirect(url_for("my_view.home",message=message))

    # An If statement is needed to display two different outcomes of task completion.

@my_view.route("/delete/<todo_id>", methods=["POST"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    message = "Task deleted"
    return redirect(url_for("my_view.home",message=message))

    # The deletion route is above.
    # One thing that would be great to add in the future is a confirmation message, to prevent accidents.