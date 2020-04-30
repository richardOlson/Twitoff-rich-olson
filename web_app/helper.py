# This file contains helper files that 
# are use to decide if a user has enough tweets 
# to be used in the app. 

from web_app.models import User, db



# This function
# will take care of removing them from the 
# database if they don't have enough tweets


def enough_tweets(num_tweets_need, db_user, statuses, screen_name):

     # if there are no tweets in the statuses
    if len(statuses) < num_tweets_need:
        db.session.delete(db_user)
        db.session.commit()
        return False
    return True