from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import base64
import config
import uuid
import aes
import hashlib
import time

index=Blueprint("index",__name__)

@index.route("/",methods=['GET', 'POST'])
def index_():
    site=config.details
    hexid=config.getCurrentPastes()
    page="Index"
    latest = config.db.pastes.find({"display":"public"}).sort("_id",-1).limit(10)
    for x in latest:
        if latest['lang'] not in config.supported:
            latest['tag'] = "default"
        else:
            latest['tag'] = latest['lang']

    if request.method == "POST":
        title = request.form['title']
        paste = request.form['paste']
        expiration = request.form['expiration']
        encryption = request.form['encryption']
        oneview = request.form.get("oneview")
        language = request.form['lang']
        display = request.form['display']
        #print language
        #print oneview
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
        if expiration:
            expiration = True
        else:
            expiration = False

        if title == "":
            title = "Untitled"
        
        if "login" in session:
            paster = session['login']
        else:
            paster = "Anonymous"
            
        config.db.pastes.insert({"paster":paster, "paste":paste, "id":id_, "title":title, "encrypted":encrypted, "password":encryption, "oneview":oneview, "lang":language, "tag":language, "expiration":expiration, "time":time.time(), "display":display})
        return redirect("/paste/{0}".format(id_))
    
    return render_template("index.html",page=page, site=site, hexid=hexid, latest=latest)
