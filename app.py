from flask import redirect, url_for, render_template, request, session, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm, UserForm
from models import db, app, User


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@login_manager.user_loader
def load_users(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/profile/", methods=["GET", "POST"])
@login_required
def profile():
    user = current_user
    name = current_user.first_name
    last_name = current_user.last_name
    return render_template('profile.html', user=user, name=name, last_name=last_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            session["logged_in"] = True
            login_user(user, remember=form.remember.data)
            next = request.args.get("next")
            return redirect(next or url_for('home'))
        flash('Невалиднa парола. Моля, опитайте пак.')
    return render_template('login.html', form=form)


@app.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if username:
            flash('Това потребителско име вече съществува')
            return redirect(url_for('register'))
        elif email:
            flash('Този имейл адрес вече съществува')
            return redirect(url_for('register'))
        username = User(username=form.username.data, email=form.email.data,
                        first_name=form.first_name.data, last_name=form.last_name.data)
        username.set_password(form.password1.data)
        db.session.add(username)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = UserForm()
    name_to_update = User.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.first_name = request.form["First Name"]
        name_to_update.last_name = request.form["Last Name"]
        name_to_update.username = request.form["username"]
        name_to_update.email = request.form["Email"]
        # name_to_update.password = request.form["Password"]
        try:
            db.session.commit()
            flash("Акаунта е редактиран успешно")
            return render_template("update.html", form=form, name_to_update=name_to_update)
        except:
            flash("Възникна грешка! Моля опитайте отново!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
        return render_template("update.html", form=form, name_to_update=name_to_update)


@app.route("/logout")
def logout():
    logout_user()
    session.clear()
    session['_remember'] = 'clear'
    return redirect(url_for('home'))


@app.route("/user_view")
@login_required
def user_view():
    return render_template("user_view.html", values=User.query.all())


@app.route("/admin/")
def admin():
    return redirect(url_for("home", name="Admin"))


# @app.route("/dashboard")
# @fresh_login_required
# def dashboard():
#     return render_template("dashboard.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

