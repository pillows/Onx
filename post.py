from flask import url_for, Blueprint, render_template, redirect, session, flash, request, Markup
import config
post=Blueprint("post",__name__)

		
#Eventually I'm going to have to change this to affect the GET request that should be generated for the AES key.
@post.route("/paste/<uid>",methods=['GET'])
def post_(uid):
    site=config.details
    hexid=config.getCurrentPastes()
    page="Paste"
    data = config.db.pastes.find_one({"id":uid})
    latest = config.db.pastes.find().sort("_id",-1).limit(10)

    for x in latest:
        if latest['lang'] not in config.supported:
            latest['tag'] = "default"
        else:
            latest['tag'] = latest['lang']

    if data['lang'] not in supported:
		data['tag'] = "default"
    else:
		data['tag'] = data['lang']
    
    if not data:
		return redirect("/")
    if data['encrypted']:
		return redirect("/encrypted/{0}".format(uid))
    elif data['oneview']:
		config.db.pastes.remove({"id":uid})
    return render_template("post.html",page=page,site=site, data=data, latest=latest)
