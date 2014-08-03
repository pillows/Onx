from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import config
import uuid

index=Blueprint("index",__name__)

@index.route("/",methods=['GET', 'POST'])
def index_():
    page="index"
    if request.method == "POST":
		title = request.form['title']
		paste = request.form['paste']
		expiration = request.form['expiration']
		encryption = request.form['encryption']
		oneview = request.form['oneview']
		id_ = uuid.uuid4().hex
		config.db.pastes.insert({"paste":paste, "id":id_})
		return redirect("/paste/{0}".format(id_))
    return render_template("index.html",page=page)
