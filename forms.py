from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last name')
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Вход')


class UserForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last name')
    password1 = PasswordField('Password', )
    password2 = PasswordField('Confirm Password', [EqualTo('password1')])
    submit = SubmitField("Submit")
