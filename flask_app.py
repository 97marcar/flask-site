"""Author: Marcus Carlsson, 2015"""

#import flask
from flask import Flask, render_template

#create flask-app
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def startpage():
    return render_template("index.html")

if (__name__ == "__main__"):
    app.run