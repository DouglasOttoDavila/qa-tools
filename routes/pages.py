from flask import Blueprint, render_template

page = Blueprint("pages", __name__)

@page.route("/")
def home():
    return render_template("index.html")

@page.route("/review_requirements")
def review_requirements():
    return render_template("review_requirements.html")