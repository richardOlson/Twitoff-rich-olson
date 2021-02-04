

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
from web_app.services.twitter_services import api as twitter_api
from web_app.models import User, db, Tweet
from web_app.services.basilica_service import basilica_connection
from web_app.statsmodels import train_twitter_model
from web_app.helper import enough_tweets

twitter_routes = Blueprint("twitter_routes", __name__)

# This is the method that will add a user and their tweets
# to the database
@twitter_routes.route("/user/add", methods=["GET", "POST"])
@twitter_routes.route("/users/<screen_name>/add", methods=["GET", "POST"])
def add_user_data(screen_name=None):
  
  # checking if the request form in None
  screen_name = request.form["twitter_name"]
  
  #TODO need to fetch the user info
  
  try:
    twit_user = twitter_api.get_user(screen_name)
    
  except:
    # will check why was not found in here
    return render_template("notFound.html", screen_name=screen_name)

  
  # Checking to see if there is already the user in the 
  # database doing a database query 
  db_user= User.query.get(twit_user.id) or User(id=twit_user.id)
  db_user.screen_name = twit_user.screen_name
  db_user.name = twit_user.name
  db_user.location = twit_user.location
  db_user.followers_count = twit_user.followers_count
  
  db.session.add(db_user)
  db.session.commit()
  
  print(f"getting the statuses for the user {twit_user.screen_name}")
  # getting the statuses
  statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=200, 
                                exclude_replies=True, include_rts=False)
  
 # This method will check to see if there is enough tweets and then will 
 # return true if the person was not deleted from the database.
 # will return false if the person is deleted from the database.
  if not enough_tweets(1, db_user, statuses, screen_name):
    oops_message = f"Oops!  {screen_name} doesn't appear to have enough tweets to use"
    return render_template("oops.html", oops_message=oops_message)

  # will be getting  more tweets if there are only a few
  while len(statuses) < 200:
    more_statuses = twitter_api.user_timeline(screen_name, max_id=statuses[-1].id,
                                              tweet_mode="extended", count=200, exclude_replies=True, 
                                              include_rts=False)
    if len(more_statuses) == 0: # This happens when there are no more tweets to get
      break
    # Adding all the statuses together
    statuses = statuses + more_statuses
  # While in the while loop, if there is not enough tweets at this point 3 then 
  # the person is deleted from the database
  if not enough_tweets(3, db_user, statuses, screen_name):
    oops_message = f"Oops!  {screen_name} doesn't appear to have enough tweets to use"
    return render_template("oops.html", oops_message=oops_message)

  tweets = []     
  # getting the tweets using list comprehension
  tweets = [status.full_text for status in statuses]

  # fetching the embeddings
  # basilica is now not working so will need to get another method of getting the embeddings
  # of the tweets
  embeddings = list(basilica_connection.embed_sentences(tweets, model="twitter"))
  
  #loading the new model
  for i in range(len(statuses)):
    db_tweet = Tweet.query.get(statuses[i].id) or Tweet(id= statuses[i].id)
    db_tweet.user_id = statuses[i].author.id
    db_tweet.full_text = statuses[i].full_text
    db_tweet.embedding = embeddings[i]
    db.session.add(db_tweet)
  # committing all the adds that have been done
  db.session.commit()

  message = f"{screen_name} has been succesfully added to the database" 
  print(screen_name)
  #return jsonify({"user": twit_user._json, "num_tweets": len(statuses)})
  return render_template("new_user.html", the_message=message)






# This is the route that will be called to bring up the form to 
# add a new twitter user
@twitter_routes.route("/user/add/form" ,methods=["GET", "POST"])
def user_add_form():
  return render_template("new_user.html")



# This is the route for the predictions page
# to show
@twitter_routes.route("/users/predict/form")
def prediction_page():
  # Getting the users from the database
  users = User.query.all()
  num_users = len(users)
  return render_template("predict.html", users=users, num_users=num_users)




# This is the method that will do the prediction when
# the form is filled and submitted
@twitter_routes.route("/users/predict", methods=["POST", "GET"])
def predict():

  users = User.query.all()
  num_users = len(users)

  try:
    user1 = request.form['name1']
    user2 = request.form["name2"]
    tweet = request.form["tweet"]
  except:
    the_answer = f"Something was wrong with the prediction.  Make sure all field are entered in."
    # Getting the users from the database
    
    return render_template("predict.html", the_answer=the_answer, num_users=num_users, users=users)
  
  
  # getting the embedding for the tweet
  tweet_embedding = basilica_connection.embed_sentence(tweet, model="twitter")
  #Query the users from the database
  user_1 = User.query.filter(User.screen_name == user1).one()
  user_2 = User.query.filter(User.screen_name == user2).one()

  # Getting the tweets from each person
  # This is done inside the "train_twitter_model" function in the statsmodel.py file
  theModel = train_twitter_model(user_1, user_2)


  print("Doing the prediction")
  # Using the model to make the prediction
  result = theModel.predict([tweet_embedding])
  
  the_answer = f"{result[0]} is most likely to have tweeted that"

  return render_template("predict.html", users=users, num_users=num_users, the_answer=the_answer)





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
  users = User.query.all()
  the_len = len(users)
  tweetlen = []
  if users != None:
    for user in users:
      the_tweets = user.tweets
      tweetlen.append(len(the_tweets))
  
  message = "Users currently found in our database"    
  return render_template("users.html", message=message, 
                          users=users, tweetlen=tweetlen, len=the_len)


#This is the route that is used to render the form that will allow you
# to then enter the information to add a user to the database
@twitter_routes.route("/new_user" , methods=["POST", "GET"])
def new_user_form():
    print("We are adding the user")
    return render_template("new_user.html")

# This is the route for when a twitter user name is added
# This route is initiated when the submit button is pressed in the new_user.html page
# It will have the data returned in a json type of file
@twitter_routes.route("/user_add", methods=["POST", "GET"])
def user_add():
  # here we need to make it so that we can add a twitter user and then 
  # put them in the database
  newBook = Book(username=request.form['name'])
  db.session.add(newBook)
  db.session.commit()

  
    
  flash(f"User '{newBook.username}' was successfully entered into the system ", "Success")
  return redirect(f"/")