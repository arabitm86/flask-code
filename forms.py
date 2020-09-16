from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationFrom (FlaskForm):
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2, max=20)])    
    
    email = StringField("Email", 
                        validators=[DataRequired(),Email(check_deliverability=True) ])
    password = StringField("Password", 
                           validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password =     password = StringField("Confirm Password", validators=[DataRequired(), Length(min=2, max=20), EqualTo("password")])
    
    submit_field = SubmitField("Sign Up")
                           
class LoginForm (FlaskForm):
    
    email = StringField("Email", 
                        validators=[DataRequired(),Email(check_deliverability=True) ])
    password = StringField("Password", 
                           validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField("Remember me")
    submit_field = SubmitField("Login")
                           