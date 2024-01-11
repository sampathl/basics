from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", [InputRequired(), Email()])
    password= PasswordField("Password",[InputRequired()] )
    submit= SubmitField("Login")





class SignUpForm(FlaskForm):
    name = StringField("Name", [InputRequired()])
    email= StringField("Email", [InputRequired(), Email()])
    password = PasswordField("Password", [InputRequired()])
    #confirmp = PasswordField("Confirm Password", [InputRequired()])
    submit = SubmitField("SignUp")