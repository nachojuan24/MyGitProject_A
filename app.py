from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Alex'
    friends = ['Alice', 'Bob', 'Carl', 'Daniel']
    return render_template('index.html', name=name, friends=friends)


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


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()