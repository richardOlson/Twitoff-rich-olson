
from flask import Blueprint, jsonify, request, redirect
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from web_app.statsmodels import load_model


stats_routes = Blueprint("stats_routes",  __name__)


@stats_routes.route("/stats/iris")
def iris():

    model = load_model()
    X , y = load_iris(return_X_y=True)
    return str(model.predict(X[:2, :]))

   

