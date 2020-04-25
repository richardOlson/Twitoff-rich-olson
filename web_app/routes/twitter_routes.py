

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



twitter_routes = Blueprint("twitter_routes", __name__)

# This is the method that will return the json version
# of the data
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