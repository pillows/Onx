from flask import url_for, Blueprint, render_template, redirect, session, flash, request, Markup
import config
import aes
import base64
import hashlib

encrypted = Blueprint("encrypted",__name__)

@encrypted.route("/encrypted/<uid>",methods=['GET','POST'])
def encrypted_(uid):
    site=config.site
    page = "encrypted"
    data = config.db.pastes.find_one({"id":uid})
    if not data or not data['encrypted']:
        return redirect("/")
     
    paste = data['paste']

    if request.method == "POST":
        password = hashlib.md5(request.form['password']).hexdigest()
        try:
            aes.decryptData(password, base64.b64decode(paste))
            session[uid] = password
        except ValueError:
            flash("Invalid Password.")

    if uid not in session:
        return render_template("password.html", page=page, site=site)
    else:
        data['paste'] = aes.decryptData(session[uid], base64.b64decode(paste))
        return render_template("post.html",page=page, data=data,site=site)
        if data['oneview']:
            config.db.pastes.remove({"id":uid})

