import os
from dotenv import load_dotenv
import tweepy # This is a package to interface with
              # With the twitter api

load_dotenv()


#TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
#TWITTER_API_SECRET  = os.getenv("TWITTER_API_SECRET")
#TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
#TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN")

TWITTER_API_KEY=os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET= os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN= os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET= os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET
                            )
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print(type(auth))

api = tweepy.API(auth)

if  __name__ == "__main__":
    
    print(type(api))

    # showing how to get the user from twitter
    user = api.get_user("elonmusk")

    # a statuses < a list of status> each status contains
    # info about a tweet
    statuses =  api.user_timeline("elonmusk", counts=35)
    statuses = api.user_timeline("elonmusk", tweet_mode="extended", count=35, 
                                exclude_replies=True, include_rts=False)

    
    
    # statatues are of the type tweepy.Status object
    tweets = []
    for status in statuses:
        tweets.append(status.full_text)
        print(status.full_text)
    
    print(len(tweets))