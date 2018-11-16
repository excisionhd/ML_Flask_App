from flask import Flask, render_template, Markup
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test/<string:first>/<string:last>")
def test(first=None, last=None):
    return ("Hello {} {}".format(first,last))
@app.route("/home")
@app.route("/home/<name>")
def home(name=None):
    return render_template('index.html', name=name)

   
