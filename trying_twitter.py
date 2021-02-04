# This is a file that will be used to try to use twitter 
# without tweepy.
from dotenv import load_dotenv
import os

load_dotenv() # Loading the environment variables

# getting the keys
TWIT_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

COOL_KEY = os.getenv("COOL")

if __name__ == "__main__":
    # checking the tokens and the keys to make  sure that they
    # are good
    print(f"This is the key  {TWIT_KEY}")
    print(f"This is the secret {TWITTER_API_SECRET}")
    print(f"This is the token {TWITTER_ACCESS_TOKEN}")
    print(f"This is the token secret {TWITTER_ACCESS_TOKEN_SECRET}"
    )
    print(f"This the cool key {COOL_KEY}")