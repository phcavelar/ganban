from flask import render_template, flash, redirect, url_for
from core import app
from core.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Pedro"}
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
    return render_template("index.html", title="Home", user=user, posts=posts)
#end index

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
              form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    #end if
    return render_template("login.html", title="Sign In", form=form)
#end login

