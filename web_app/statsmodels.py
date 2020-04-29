from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from web_app.models import User , Tweet , db
# Will use the picke to load the file 
import pickle
import os

#Path where the model will be saved
MODEL_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, "predictive_models", "saved_model.pkl")

# used to train the iris and save it
def train_model_and_save():
    print("Training the model")
    X, y = load_iris(return_X_y=True)
    classifier = LogisticRegression(random_state=49, max_iter=150)
    classifier.fit(X, y)

    # Saving the model
    with open(MODEL_PATH, "wb") as model:
        pickle.dump(classifier, model)
        
    return classifier

# Will return the trained model. Will read it to a 
# file
def load_model():
    # Will load the model from the file
    with open(MODEL_PATH, "rb") as model:
        the_model = pickle.load(model)
    
    return the_model

# This is the method that will be used to train the 
# for the twitter prediction
def train_twitter_model(user1, user2):

    classifier = LogisticRegression(random_state=49, solver="lbfgs", multi_class="multinomial")
    # will get the embeddings and the screen name for the 
    # two different  users
    embeddings = []
    screen_names = []

    classifier.fit(embeddings, screen_names)
    # returning the model to do the prediction
    return classifier
    
    

if __name__ == "__main__":
    train_model_and_save()

    load_model()

