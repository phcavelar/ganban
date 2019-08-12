from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from core import app, db
from core.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from core.models import User

@app.route("/")
@app.route("/index")
@login_required
def index():
    posts = [
        {
          "author": {"username": "Pedro"},
          "body": "Viols é linda."
        },
        {
          "author": {"username": "Viols"},
          "body": "Me leva pra passear!"
        }
    ]
    return render_template("index.html", title="Home", posts=posts)
#end index

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    #end if
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("index"))
        #end if
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        #end if
        return redirect(next_page)
    #end if
    return render_template("login.html", title="Sign In", form=form)
#end login

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
#end logout

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    #end if
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now registered!")
        return redirect(url_for("login"))
    #end if
    return render_template("register.html", title="Register", form=form)
#end register
