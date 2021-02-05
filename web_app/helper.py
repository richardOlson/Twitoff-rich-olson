# This file contains helper files that 
# are use to decide if a user has enough tweets 
# to be used in the app. 


# Also will contain the code where the nlp object for spacy is found

from web_app.models import User, db
import spacy
import en_core_web_md


# This is the global variable
# This variable will hold the instance of the NLP class when the 
# function "build_class" is called
nlp_global = None


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


# making a class that will hold the nlp object and this will be used to get the 
# embeddings for the database to use.  With this class we will no longer use the
# basilica api (as it is no longer present)
class NLP:
    
    def __init__(self, ):
        self.nlp = self.get_nlp()

    # below is the addition of the use of spacy so that we can then get the word embeddings of some 
    # sentances
    # This is the function that will be used to create the nlp so that it can be used
    def get_nlp(self):
        nlp = en_core_web_md.load()
        return nlp



    # function for the returning of a embedding 
    # This function will return a list if a list of embeddings if
    # a list is given to it or will just return a single embedding vector of 300 shape
    # if a single sentance is given to it
    def get_embedding(self, doc: str):
        the_document = self.nlp(doc)
        return the_document.vector
    # 

# This the function that will be called in the init that will make an
# instance of the nlp class.
def build_class():
    nlp_global = NLP()

if __name__ == "__main__":
    nlp = get_nlp()
    print(type(nlp))