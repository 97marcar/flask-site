"""Author: Marcus Carlsson, 2015"""

#import flask
from flask import Flask, render_template, flash

#create flask-app
app = Flask(__name__)

@app.route('/')
@app.route('/startpage/')
def startpage():
    """..."""
    flash("This site uses cookies")
    return render_template("startpage.html")

if (__name__ == "__main__"):
    app.run
