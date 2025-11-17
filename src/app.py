from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increase", methods=["POST"])
def increase():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/increment", methods=["POST"])
def increment():
    value = request.form["title"]
    intvalue = int(value)
    cnt.reset()
    cnt.increment(intvalue)
    return redirect("/")
