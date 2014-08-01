from flask import Flask, session, redirect
from index import index
from login import login
#from register import register
import config

app = Flask(__name__)
app.secret_key = "ASD'l1l;23k123kk;laskd;askd;lakSD;;alsmmzxcmmadf;kas;DK;lkl;1;23k1;23k;SAd00123lal;sdk;SAKD;lk213123"
app.debug = True
port = 5000

app.register_blueprint(index)
app.register_blueprint(login)
#app.register_blueprint(register)

@app.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=port)
