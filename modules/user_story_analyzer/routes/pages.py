from flask import Blueprint, render_template

rr_page = Blueprint("rr_page", __name__)

@rr_page.route("/review_requirements")
def review_requirements():
    return render_template("review_requirements.html")