
# importing the blueprint class into here
from flask import Blueprint, render_template
from web_app.models import User

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    print("Have come to the home page")
    #return render_template("users.html", message=message, users=users)
    message = "Welcome to my Twittoff app.  An app to guess which twitter user would say a certain tweet!\n"
    # Finding out if we have some users to do prediction 
    # with
    users = User.query.all()
    num_users = len(users)
    
    return render_template("predict.html", message=message, num_users=num_users, users=users)
#
#@home_routes.route("/about")
#def about():
#    print("Just called the about route method")
#    return f"TODO"


@home_routes.route("/home")
def display_oops():
    oops_message = "Oops, you don't have authorization for that"
    return render_template("oops.html", oops_message=oops_message)

