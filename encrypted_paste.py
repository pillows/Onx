from flask import url_for, Blueprint, render_template, redirect, session, flash, request, Markup
import config
import aes
import base64

encrypted = Blueprint("encrypted",__name__)

@encrypted.route("/encrypted/<uid>",methods=['GET','POST'])
def encrypted_(uid):
    site=config.site
    page = "encrypted"
    data = config.db.pastes.find_one({"id":uid})
    #print data['lang']
    data['paste']=Markup(highlight(data['paste'], get_lexer_by_name(data['lang']), HtmlFormatter(linenos=True)))
    if not data:
        return redirect("/")
    return render_template("post.html",page=page, data=data,site=site)


