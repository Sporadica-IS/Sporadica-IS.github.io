# Started on 5/08/2020 at 16:33
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/kayos/user/<username>")
def show_user_profile(username):
	pass