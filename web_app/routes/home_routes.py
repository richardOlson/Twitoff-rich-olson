
# importing the blueprint class into here
from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)


#@home_routes.route("/")
#def index():
    print("Have come to the home page")
    #return render_template("users.html", message=message, users=users)
    message = "Welcome to my Twittoff app.  An app to guess which twitter user would say a certain tweet!\n"
    return render_template("home.html", message=message)
#
#@home_routes.route("/about")
#def about():
#    print("Just called the about route method")
#    return f"TODO"

