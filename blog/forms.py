from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms_validators import AlphaNumeric

class RegistrationFrom (FlaskForm):
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2, max=20), AlphaNumeric()])    
    
    email = StringField("Email", 
                        validators=[DataRequired(),Email(check_deliverability=True) ])
    password = PasswordField("Password", 
                           validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField("Confirm Password", 
                            validators=[DataRequired(), Length(min=2, max=20), EqualTo("password"), ])
    
    submit = SubmitField("Sign Up")
                           
class LoginForm (FlaskForm):
    
    email = StringField("Email", 
                        validators=[DataRequired(),Email(check_deliverability=True) ])
    password = PasswordField("Password", 
                           validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
                           