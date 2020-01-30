from flask import Flask, render_template, redirect, request
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import Task

app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)

@app.route('/', methods=['POST', 'GET',])
def get_tasks():
    if request.method == 'POST':
        task_obj = Task(task_name=request.form.get("taskname"))
        db.session.add(task_obj)
        db.session.commit()
    tasks_qs = Task.query.all()
    return render_template('list.html', tasks=tasks_qs)

@app.route('/<int:task_id>/update', methods=['POST', 'GET',])
def update(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.task_name = request.form.get("taskname")
        db.session.commit()
        return redirect('/')
    
    return render_template("update.html", task=task)

@app.route('/<int:task_id>/delete', methods=['GET'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')
    




if __name__ == '__main__':
    app.run()