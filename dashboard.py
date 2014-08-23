from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
dashboard=Blueprint("dashboard",__name__)

@dashboard.route("/dashboard",methods=['GET','POST'])
def dashboard_():
    page="dashboard"
    if "login" not in session:
        return redirect("/")
    pastes = config.db.pastes.find({"paster":session['login']})
    if request.method == "POST":
        id_ = request.form['delete']
        paste = config.db.pastes.find_one({"id":id_})
        if paste['paster'] == session['login']:
            config.db.pastes.remove({"id":id_})
        else:
            return "Nice try"
    return render_template("login.html",page=page, pastes=pastes)
