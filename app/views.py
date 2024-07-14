from flask import current_app as app
from flask import render_template


@app.route("/")
def hello_world():
    return render_template("home.html")
