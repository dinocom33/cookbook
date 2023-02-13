import os
from datetime import timedelta, datetime

from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["USE_SESSION_FOR_NEXT"] = True
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)
db.init_app(app)
admin = Admin(app, template_mode="bootstrap3")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique=True, index=True)
    first_name = db.Column(db.String(150), index=True)
    last_name = db.Column(db.String(150), index=True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notify.html')


class ExitAdmin(BaseView):
    @expose("/")
    def exit(self):
        return self.render("/index.html")


admin.add_view(ModelView(User, db.session))
admin.add_view(NotificationsView(name="Notifications", endpoint="notify"))
admin.add_view(ExitAdmin(name="Exit", endpoint="/index"))
