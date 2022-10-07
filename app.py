import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# set the correct paths to the root directory and local database file
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

app = Flask(__name__)
# Initialize the database to be used with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)

# making each todo item have a column number, a title, and a boolean marking completeness
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

# the index url, which all actions are redirected to
@app.route("/")
def index():
    # Get all the todo objects in a list
    todo_list = Todo.query.all()
    # Find the total number of todos
    length = len(todo_list)
    # increment over each todo, checking if it is complete, and incrementing a counter for the number of incomplete tasks
    incomplete = 0
    for todo in todo_list:
        if todo.complete == False:
            incomplete += 1
    # show the index.html page with the correct variables passed in
    return render_template("index.html", todo_list=todo_list, incomplete=incomplete, length=length)

# post method for this add function, only called when new item is added
@app.route("/add", methods=["POST"])
def add():
    # only thing to set is the user inputted title of the todo
    title = request.form.get("title")
    # Create a todo object using the defaults plus the title
    new_todo = Todo(title=title, complete=False)
    # add the todo to the list
    db.session.add(new_todo)
    db.session.commit()
    # redirect to the index
    return redirect(url_for("index"))

# marking a particular todo as complete when it is clicked
@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    # selecting the correct todo in the list by the id of what was clicked
    todo = Todo.query.filter_by(id=todo_id).first()
    # reverse the boolean to change marking of completeness
    todo.complete = not todo.complete
    db.session.commit()
    # redirect to the index
    return redirect(url_for("index"))

# deleting an item from the database when delete is clicked
@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    # selecting the correct todo in the list by the id of what was clicked
    todo = Todo.query.filter_by(id=todo_id).first()
    # delete the todo from the database
    db.session.delete(todo)
    db.session.commit()
    # redirect to the index
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
