from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/features')
def features():
    return '<h1>Learn about our features</h1>!'

@app.route('/about')
def about():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()