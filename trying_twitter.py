# This is a file that will be used to try to use twitter 
# without tweepy.
from dotenv import load_dotenv
import os
import en_core_web_md

load_dotenv() # Loading the environment variables

# getting the keys
TWIT_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Trying out the nlp function to see how to work with it.
def get_nlp():
    nlp = en_core_web_md.load()
    return nlp


# these is a sentence that we will play with
first_string = "This is such fun!"
second_string = "I like to eat cake."
third_string = "I want a hamburger."

if __name__ == "__main__":
    # checking the tokens and the keys to make  sure that they
    # are good
    nlp = get_nlp()

    first_doc = nlp(first_string)
    second_doc = nlp(second_string)
    third_doc = nlp(third_string)
    breakpoint()
    print(f"This is the first doc and this is the vector shape of the complete sentance {first_doc.vector}")