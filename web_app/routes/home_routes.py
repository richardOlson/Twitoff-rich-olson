
# importing the blueprint class into here
from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    print("In the home route")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("Just called the about route method")
    return f"TODO"

