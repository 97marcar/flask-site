"""Author: Marcus Carlsson, 2015"""

#import flask
from flask import Flask, render_template, flash
from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtform.validator import DataRequired, Length, EqualTo
import sqlite3 as lite

#configure för flask
DATABASE = "flask-site/database/testdb.db"
DEBUG = True
SECRET_KEY = "]£€[JNASFU=()]___???!###¤¤¤"
USERNAME = "admin"
PASSWORD = "default"

#create flask-app
app = Flask(__name__)

#init database
def initdv():
    try:
        con = lite.connect(app.config['DATABASE'])
        cur = con.cursor()
        cur.execute("""CREATE TABLE users(
        uid INTEGER PRIMARY KEY NOT NULL,
        username VARCHAR(10),
        email VARCHAR(30),
        password VARCHAR(10),
        role VARCHAR(10),
        )""")
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        return e

@app.route('/')
@app.route('/startpage/')
def startpage():
    """..."""
    #flash("This site uses cookies")
    return render_template("startpage.html")
class RegistrationForm(Form):
    """docstring for RegistrationForm"""
    def __init__(self, arg):
        super(RegistrationForm, self).__init__()
        self.arg = arg

@app.route('/register/', methods = ["GET", "POST"])
def register():
    try:
        form = RegistrationForm(request.form)
    except:
        pass
if (__name__ == "__main__"):
    app.run
