
from flask import Blueprint, jsonify, request, redirect
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from web_app.statsmodels
stats_routes = Blueprint("stats_routes",  __name__)


@stats_rountes.route("/stats/iris")
def iris():

    X, y = load_iris(return_X_y=True)
   

