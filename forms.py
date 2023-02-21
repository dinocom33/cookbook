from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name = StringField("First Name")
    last_name = StringField("Last name")
    password1 = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=20)],
                              render_kw={"placeholder": "Password"})
    password2 = PasswordField("Confirm Password", validators=[DataRequired(),
                                                              EqualTo("password1", message="Паролите трябва да съвпадат")])
    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    # email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Запомни ме")
    submit = SubmitField("Вход")


class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField("Email", validators=[DataRequired(), Email()])
    first_name = StringField("Име")
    last_name = StringField("Фамилия")
    password1 = PasswordField("Password")
    password2 = PasswordField("Confirm Password", [EqualTo("password1")])
    submit = SubmitField("Потвърди")
