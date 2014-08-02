from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
register=Blueprint("register",__name__)

@register.route("/register",methods=['GET','POST'])
def register_():
    page="register"
    if request.method == "POST":
        username = request.form['login'].lower()
        password = config.protect(request.form['password'])
        confirm = config.protect(request.form['cpassword'])
        email = request.form['email']
        cemail = request.form['cemail']
        if password != confirm:
            flash("Passwords do not match")
            return redirect("/register")
        elif email != cemail:
            flash("Emails do not match")
            return redirect("/register")
        else:
            config.db.members.insert({"username":username, 'password':password, "email":email})
            session['login'] = username
            return redirect("/")

    return render_template("register.html",page=page)
