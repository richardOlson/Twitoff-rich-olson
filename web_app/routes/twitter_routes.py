

# In here we will have the tweet routes for 
# tweets.
# Will want a route that will has a form  to add
# a user and a tweet.
# Will also want a route that will display the users 
# and then will display all their tweets

# doing the imports
from flask import Flask, jsonify , render_template , request
from flask import Blueprint, flash, redirect
from web_app.models import db , Book
from web_app.services.twitter_services import api as twiiter_api
from web_app.models import User, db, Tweet


twitter_routes = Blueprint("twitter_routes", __name__)

# This is the method that will return the a users data
@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
  
  #TODO need to fetch the user info
  user = twitter_api.get_user(screen_name)

  # Checking to see if there is already the user in the 
  # database doing a database query 
  db_user= User.query.get(twitter_user.id) or User(id=user.id)
  db_user.screen_name = user.screen_name
  db_user.name = user.name
  db_user.location = user.location
  db_user.folowers_count = user.folowers_count
  db.session.add(db_user)
  db.session.commit()
  # getting the statuses
  statuses = twiiter_api.user_timeline(screen_name, tweet_mode="extended", count=35, 
                                exclude_replies=True, include_rts=False)
  # putting this in a database if they are not there

  print(screen_name)
  return jsonify({"user": user._json, "num_tweets": len(statuses)})


# This is the method that will return the json version
# of the data of all the users
@twitter_routes.route("/twitter_users.json")
def list_users_json():
  #users = [
  #    {"name": "John Doe"},
  #    {"name": "Joe Blow"},
  #    {"name": "Me"}

  #]
  
  return jsonify(users)

# This is the funtion that will allow the return of the
# data but in a HTML page
@twitter_routes.route("/twitter_users" , methods=["GET", "POST"])
def list_users():
   #users = [
   #    {"name": "John Doe"},
   #    {"name": "Joe Blow"},
   #    {"name": "Me"}

   #]
    book_records = Book.query.all()
    
    message = "Users currently found in our database"
    return render_template("users.html", message=message, users=book_records)


#This is the route that is used to render the form that will allow you
# to then enter the information to add a user to the database
@twitter_routes.route("/new_user" , methods=["POST", "GET"])
def user_form():
    print("We are adding the user")
    return render_template("new_user.html")

# This is the route for when a twitter user name is added
# This route is initiated when the submit button is pressed in the new_user.html page
# It will have the data returned in a json type of file
@twitter_routes.route("/user_add", methods=["POST", "GET"])
def user_add():
    newBook = Book(username=request.form['name'])
    db.session.add(newBook)
    db.session.commit()
    
    flash(f"User '{newBook.username}' was successfully entered into the system ", "Success")
    return redirect(f"/")