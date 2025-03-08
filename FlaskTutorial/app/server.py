from flask import Flask
from flask import render_template
from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = "Ali"
    return render_template("index.html", title=" welcome", username=name)


@app.route("/dashboard/<name>")
def dashboard(name):
    return "welcome %s" % name


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("dashboard", name=user))
    else:
        user = request.args.get("name")
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)


app.run()
