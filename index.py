from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import base64
import config
import uuid
import aes
import hashlib

index=Blueprint("index",__name__)

@index.route("/",methods=['GET', 'POST'])
def index_():
    site=config.site
    page="Index"
    if request.method == "POST":
		title = request.form['title']
		paste = request.form['paste']
		expiration = request.form['expiration']
		encryption = request.form['encryption']
		oneview = request.form.get("oneview")
		language = request.form['lang']
		print oneview
		id_ = uuid.uuid4().hex
                if encryption:
                    encrypted = True
                    encryption = hashlib.md5(encryption).hexdigest()
                    paste = base64.b64encode(aes.encryptData(encryption, paste))
                else:
                    encrypted = False
                if oneview:
                    oneview = True
                else:
                    oneview = False

                config.db.pastes.insert({"paste":paste, "id":id_, "title":title, "encrypted":encrypted, "password":encryption, "oneview":oneview, "lang":language})
		return redirect("/paste/{0}".format(id_))
    return render_template("index.html",page=page, site=site)
