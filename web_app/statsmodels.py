from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
# Will use the picke to load the file 
import pickle
import os

#Path where the model will be saved
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "saved_model.pkl")

# Will return the trained model. Will read it to a 
# file
def load_model()


def train_model_and_save():
    print("Training the model")
    X, y = load_iris(return_X_y=True)
    classifier = LogisticRegression()
    classifier.fit(X, y)

    # Saving the model
    #with open(MODEL_PATH, "wb") as mo
