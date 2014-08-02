from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
login=Blueprint("login",__name__)

@login.route("/login",methods=['GET','POST'])
def login_():
    page="login"
    if request.method == "POST":
        username = request.form['login']
        password = config.protect(request.form['password'])
        if config.db.members.find_one({"username":username, "password":password}):
            session['login'] = username
            return redirect("/")
        else:
            flash("Login invalid")
            return redirect("/login")
    return render_template("login.html",page=page)
