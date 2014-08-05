from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
import aes
import base64

encrypted = Blueprint("encrypted",__name__)

@encrypted.route("/encrypted/<uid>",methods=['GET','POST'])
def encrypted_(uid):
    page = "encrypted"
    data = config.db.pastes.find_one({"id":uid})
    if not data:
        return redirect("/")
    return render_template("post.html",page=page, data=data)


