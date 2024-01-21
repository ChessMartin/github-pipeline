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
    ref = payload.get('ref', '')

    print(ref)
    if ref == 'refs/heads/testing':
        print("Push to testing branch detected. Implement your logic here.")

    return 'Webhook received', 200  # Sending a 200 response to GitHub

@app.route('/deploy', methods=['POST'])
def deploy():
    payload = request.json
    ref = payload.get('ref', '') if payload else ''

    if ref == 'refs/heads/main':
        subprocess.run(["./deployment_script.sh"])
        print("Deployment script executed.")

    return 'Deployment webhook received', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
