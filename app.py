from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello World! </h1>'


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age=None):
    if name==None and age==None:
        return '<h2> Hello world! </h2>'
    elif age == None:
        return f'<h2> Hello {name}! </h2>'
    else:
        return f'<h2> Hello {name}! Two times your age is {age*2}, right? </h2>'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()