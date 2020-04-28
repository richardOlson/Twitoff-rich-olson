

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
import os
from web_app.models import db, migrate


# Creating the path to the database that we will use
# C:\Users\porte\Richard_python\lambda\lam3\Twitoff-rich-olson
DATABASE_URI = "sqlite:///C:\\Users\\porte\\Richard_python\\lambda\\lam3\\Twitoff-rich-olson\\twitter_development.db"
SECRET_KEY = 'super secret'




# creating the app the an app factory
def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    return app








# Will go into here to start to run the module of 
# the application
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
