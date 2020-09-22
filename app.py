from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)

#generated from python 'import secrets.token_hex(16)
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
