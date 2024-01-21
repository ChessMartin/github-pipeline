from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)
todos = []

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        todo_item = request.form.get('todo_item')
        if todo_item:
            todos.append(todo_item)

    return render_template_string("""
        <!doctype html>
        <html>
            <head>
                <title>To-Do List</title>
            </head>
            <body>
                <h1>To-Do List</h1>
                <form method="post">
                    <input type="text" name="todo_item" />
                    <input type="submit" value="Add"/>
                </form>
                <ul>
                    {% for todo in todos %}
                        <li>{{ todo }}</li>
                    {% endfor %}
                </ul>
            </body>
        </html>
    """, todos=todos)

@app.route('/testing', methods=['POST'])
def testing():
    payload = request.json
    ref = payload.get('ref', '') if payload else ''
    print("Printed from the testing endpoint")

    if ref == 'refs/heads/staging':
        print("Running the testing script from the endpoint")
        subprocess.run(["./testing_script.sh"])

    return 'Webhook received', 200

@app.route('/deploy', methods=['POST'])
def deploy():
    payload = request.json
    ref = payload.get('ref', '') if payload else ''
    print("Printed from the testing endpoint")

    if ref == 'refs/heads/staging':
        print("Running the deployement script from the endpoint")
        subprocess.run(["./deployment_script.sh"])

    return 'Deployment webhook received', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
