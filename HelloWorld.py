from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/info.html')
def info():
    return 'info.html!'

@app.route('/info2.html')
def info2():
    return 'Welcome to my world!'

@app.route('/info3.html')
def info3():
    return 'this is info3.html'
@app.route('/info4.html')
def info3():
    return 'this is info4.html'
if __name__ == '__main__':
    app.run()
