from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

# create database
class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')

# create extension
db = SQLAlchemy(model_class=Base)

# initialise the database
db.init_app(app)

#create table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)

with app.app_context():
    db.create_all()


class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    date = DateField('Task Date', format='%Y-%m-%d')
    time = TimeField('Task Time', format='%H:%M')
    submit = SubmitField('Submit')

@app.route('/')
def home():
    results = db.session.execute(db.select(Todo).order_by(Todo.id))
    all_todos = results.scalars()
    return render_template("index.html", todos=all_todos)

@app.route('/add', methods=["GET", "POST"])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        todos = Todo(
            task=form.task.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(todos)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route('/edit/<todo_id>', methods=["GET", "POST"])
def edit(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    edit_form = TodoForm(
        task=todo.task,
        date=todo.date,
        time=todo.time
    )

    if edit_form.validate_on_submit():
        todo.task=edit_form.task.data
        todo.date=edit_form.date.data
        todo.time=edit_form.time.data

        db.session.commit()
        return redirect(url_for("home", todo_id=todo.id))
    return render_template("add.html", form=edit_form, is_edit=True)
    

@app.route('/delete/<todo_id>')
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)