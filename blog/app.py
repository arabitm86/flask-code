from datetime import datetime
import sys
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationFrom, LoginForm

app = Flask(__name__, template_folder='../templates', static_folder='../static')

#generated from python 'import secrets.token_hex(16)
app.config['SECRET_KEY'] = "5a6b405ff353b94ffe92838db151d58b"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
    
"""Convert all the above to args and pass via deployment using configmap"""

#app.config['test'] = sys.argv[1]
#print (app.config['test'])

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    #hash value 60 char long
    password = db.Column(db.String(60), nullable=False)
    
    #create one to many relationship, backref allows us to use the author attribute to get the user who
    #created the post, this wont be an additional column its a relationship
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
    
posts = [
    
    {"author":"Author1",
     "title":"Title1",
     "content":"Some content",
     "date" : "April 28th 2018"
     },
    
    {"author":"Author2",
     "title":"Title2",
     "content":"Some content",
     "dats" : "May 28th 2018"
     }    
]
@app.route("/")
@app.route("/home")
def home ():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about ():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register ():
    registrationForm = RegistrationFrom()
    #use flash message to sucess or error out visually to the user and 'success' comes from bootstrap
    if registrationForm.validate_on_submit():
        flash(f'Account created for {registrationForm.username.data}!', 'success')
        #redirect user to home page on succcessful registration
        return redirect(url_for('home'))
    return render_template('registration.html', title='Registration', form=registrationForm)

@app.route("/login", methods=['GET', 'POST'])
def login ():
    loginForm = LoginForm()
    return render_template('login.html', title='Login', form=loginForm)

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
    
