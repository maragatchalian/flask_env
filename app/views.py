from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mara'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': '@ericjandale'}, 
            'body': 'I am a Marine Engineer!' 
        },
        { 
            'author': {'nickname': '@marsgatchalian'}, 
            'body': 'I am inlove with a Marine Engineer!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)