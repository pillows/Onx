from flask import url_for, Blueprint, render_template, redirect, session, flash, request, Markup
from pygments import highlight, util
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
import config
post=Blueprint("post",__name__)

		
#Eventually I'm going to have to change this to affect the GET request that should be generated for the AES key.
@post.route("/paste/<uid>",methods=['GET'])
def post_(uid):
    site=config.site
    page="Paste"
    supported=['php','text','boo','cpp','c','ruby','rust', 'diff', 'erlang', 'lua', 'js', 'bash', 'go']
    data = config.db.pastes.find_one({"id":uid})
	
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
    return render_template("post.html",page=page,site=site, data=data)
