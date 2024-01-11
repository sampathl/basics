from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", [InputRequired(), Email()])
    password= PasswordField("Password",[InputRequired()] )
    submit= SubmitField("Login")