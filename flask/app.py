from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index(): 
    title = 'Tadaa to do list app'
    name = ['ken''john']
    fake_number = '356'
    
    return render_template('index.html', title=title, name=name, visitor_number = fake_number)

@app.route('/cookies/<slug>')
def cookie(slug):
  return slug + ' ' + request.args.get('name')

@app.route('/features')
def features():
    return "<a href=\"/features\">features</a>"
    

@app.route('/about')
def about():
    return "<a href=\"/about\">about</a>"

if __name__ == '__main__':
    app.run()