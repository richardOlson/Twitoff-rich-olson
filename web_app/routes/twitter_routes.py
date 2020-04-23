

# In here we will have the tweet routes for 
# tweets.
# Will want a route that will has a form  to add
# a user and a tweet.
# Will also want a route that will display the users 
# and then will display all their tweets

# doing the imports
from flask import Flask, jsonify , render_template
from flask import Blueprint



twitter_routes = Blueprint("twitter_routes", __name__)

# This is the method that will return the json version
# of the data
@twitter_routes.route("/twitter_users.json")
def list_users_json():
    users = [
        {"name": "John Doe"},
        {"name": "Joe Blow"},
        {"name": "Me"}

    ]
    return jsonify(users)

# This is the funtion that will allow the return of the
# data but in a HTML page
@twitter_routes.route("/twitter_users")
def list_users():
    users = [
        {"name": "John Doe"},
        {"name": "Joe Blow"},
        {"name": "Me"}

    ]
    message = "Users currently found in our database"
    return render_template("users.html", message=message, users=users)


#This is the route that is used to add a new user to the database
@twitter_routes.route("/new_user")
def add_user():
    print("We are adding the user")
    return render_template("new_user.html")