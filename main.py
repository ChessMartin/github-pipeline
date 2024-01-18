from flask import Flask, request, render_template_string

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
