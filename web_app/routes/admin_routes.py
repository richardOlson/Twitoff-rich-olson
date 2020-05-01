from flask import Blueprint, jsonify, request, redirect, flash, render_template
from web_app.models import db, migrate, User , Tweet
from dotenv import load_dotenv
import os


load_dotenv()

# Getting the api key this is for local
#API_KEY = os.getenv("API_KEY")

# this is for production
API_KEY = "abc123"

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
    return jsonify({"message":"DB RESET OK"})


@admin_routes.route("/admin/remove/<screen_name>", methods=["GET", "POST"])
def remove_one(screen_name):

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:

        
        user = User.query.filter(User.screen_name == screen_name).one()
        # if it can't find the user in the database
        if user == None:
            mess = f"{screen_name} does not seem to be in the database.  Make sure you spelled it correctly"
            return render_template("oops.html", oops_message=mess )
        tweets = user.tweets

        if tweets != None and len(tweets) > 0:
            for tweet in tweets:
                db.delete(tweet)
            db.commit()
        
        db.delete(user)
        db.commit()
        mess = f"{screen_name} was removed from the database!"
        return render_template("oops.html", oops_message=mess)
    
    mess = f"You don't have the security access to do that"
    return render_template("oops.html", oops_message=)
