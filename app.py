from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

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
    
    # print(url_for('index'))
    # print(url_for('hello', name='Alex', age=27))
    # print(url_for('code', code = 'print("Hola")'))

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

#Create a form with wtform
class ResgisterForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField("Sign up ")

# Register user
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = ResgisterForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Username: {username}, Password: {password}"

    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password)<=40:
    #         return f"Username: {username}, Password: {password}"
    #     else:
    #         error = """The username must have between 4 and 25 characters. 
    #         The password must also have between 6 and 40 characters."""

    #         return render_template('auth/register.html', form=form, error = error)
        
    return render_template('auth/register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()