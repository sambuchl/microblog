from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sam'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Frigid day in Mantorville!'
        },
        {
            'author': {'username': 'Linda'},
            'body': 'Busy day at Mayo!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
