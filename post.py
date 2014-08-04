from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
post=Blueprint("post",__name__)

#Eventually I'm going to have to change this to affect the GET request that should be generated for the AES key.
@post.route("/paste/<uid>",methods=['GET'])
def post_(uid):
    page="paste"
    data = config.db.pastes.find_one({"id":uid})
    if not data:
        return redirect("/")
    if data['encrypted']:
        return redirect("/encrypted/{0}".format(uid))
    elif data['oneview']:
        config.db.pastes.remove({"id":uid})
    return render_template("post.html",page=page, data=data)
