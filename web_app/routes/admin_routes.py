from flask import Blueprint, jsonify, request, redirect, flash
from web_app.models import db, migrate
from dotenv import load_dotenv
import os

load_dotenv()

# Getting the api key
API_KEY = os.getenv("API_KEY")

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        db.drop_all()
        db.create_all()

    else:
       # flash("OOPS Permission Denied", "danger")
        return redirect("/home")
    return jasonify({"message":"DB RESET OK"})