from flask import Flask, render_template, url_for
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "5a6b405ff353b94ffe92838db151d58b"

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

@app.route("/register")
def register ():
    registrationForm = RegistrationFrom()
    return render_template('registration.html', title='Registration', form=registrationForm)

@app.route("/login")
def login ():
    loginForm = LoginForm()
    return render_template('login.html', title='Login', form=loginForm)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
