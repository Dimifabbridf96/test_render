from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
@app.route('/')
def index():
    return  render_template('index.html')


@app.route("/tasks")
def tasks_list():
    return render_template('tasks.html', tasks=tasks)

@app.route("/add")
def task_list():
    return render_template('add_task.html')

@app.route("/add", methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        task = request.form.get("task")
        tasks.append(task)
        return redirect(url_for('tasks_list'))
    return render_template('add_task.html')