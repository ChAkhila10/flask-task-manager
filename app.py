from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        task = request.form.get('task')

        if task:

            tasks.append({
                "task": task,
                "done": False
            })

        return redirect('/')

    # Task counters
    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:

        if task['done']:
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    return render_template(
        'index.html',
        tasks=tasks,
        total=total_tasks,
        completed=completed_tasks,
        pending=pending_tasks
    )


@app.route('/delete/<int:index>')
def delete(index):

    tasks.pop(index)

    return redirect('/')


@app.route('/complete/<int:index>')
def complete(index):

    tasks[index]['done'] = True

    return redirect('/')


@app.route('/clear')
def clear():

    tasks.clear()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
