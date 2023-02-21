from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField("Потребителско име", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField("Имейл", validators=[DataRequired(), Email()])
    first_name = StringField("Име")
    last_name = StringField("Фамилия")
    password1 = PasswordField("Парола", validators=[InputRequired(), Length(min=8, max=20)],
                              render_kw={"placeholder": "Password"})
    password2 = PasswordField("Потвърди парола", validators=[DataRequired(),
                                                              EqualTo("password1", message="Паролите трябва да съвпадат")])
    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    # email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Потребителско име", validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField("Парола", validators=[DataRequired()])
    remember = BooleanField("Запомни ме")
    submit = SubmitField("Вход")


class UserForm(FlaskForm):
    username = StringField("Потребителскo име", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder": "Username"})
    email = StringField("Имейл", validators=[DataRequired(), Email()])
    first_name = StringField("Име")
    last_name = StringField("Фамилия")
    password1 = PasswordField("Password")
    password2 = PasswordField("Confirm Password", [EqualTo("password1")])
    submit = SubmitField("Потвърди")
