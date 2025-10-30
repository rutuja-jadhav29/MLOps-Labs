from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Internal URL for backend service inside Docker
BACKEND_URL = "http://spring-boot-app:8080/tasks"

@app.route('/')
def home():
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
        tasks = data.get("tasks", [])
    except Exception as e:
        print("Error fetching tasks:", e)
        tasks = []
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    print(f"Adding task: {task}")
    if task:
        try:
            r = requests.post(BACKEND_URL, json={'task': task})
            print("Backend response:", r.status_code, r.text)
        except Exception as e:
            print("Error posting task:", e)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        requests.delete(f"{BACKEND_URL}/{task_id}")
    except Exception as e:
        print("Error deleting task:", e)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
