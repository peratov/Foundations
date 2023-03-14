from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder="templates")
app.config.from_object('config')

todos = [{"task": "Sample Todo", "done": False}]
#{"todo": "jddd", "done"}

#Default root route rendering html page with css
@app.route('/')
def index(): 
    title = 'Tadaa to do list app'
    name = ['ken''john']
    fake_number = '356'
    return render_template('index.html', title=title, name=name, visitor_number = fake_number, todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])

def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form['todo']
        return redirect(url_for(('index')))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] =not todos [index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos [index]
    return redirect(url_for('index'))

#Dynamic Route
@app.route('/features/<slug>')
def features(slug):
    return slug
    return "<a href=\"/features\">features</a>"
    

@app.route('/about')
def about():
    return "<a href=\"/about\">about</a>"

if __name__ == '__main__':
    app.run()