from flask import Flask, render_template, url_for
from markupsafe import escape
from datetime import datetime

app = Flask(__name__)

#Filters
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# app.add_template_filter(today, 'today')

# Personalized Functions
@app.add_template_global
def repeat(s, n):
    return s*n

# app.add_template_global(repeat, 'repeat')

@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name='Alex', age=27))
    print(url_for('code', code = 'print("Hola")'))

    name = 'Alex'
    friends = ['Alice', 'Bob', 'Carl', 'Daniel']
    date = datetime.now()
    return render_template(
        'index.html',
         name=name,
         friends=friends,
         date=date
    )


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age=None, email=None):
    my_data = {
        'name': name, 
        'age': age, 
        'email': email
    }
    return render_template('hello.html', data = my_data)


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()