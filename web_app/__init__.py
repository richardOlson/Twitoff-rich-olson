

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.stats_route import stats_routes
import os
from web_app.models import db, migrate
from dotenv import load_dotenv


load_dotenv()

# going to use the os to make the path for the database
# Creating the path to the database that we will use
# C:\Users\porte\Richard_python\lambda\lam3\Twitoff-rich-olson
# will make the enviroment variable for the database url
# will comment this out this part below if for only when 
# in local production
DATA_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, "twitter_development.db" )
DATABASE_URL = "sqlite:///" + DATA_PATH


# This part below is for only when in production on the server
# needs to be commented out when run locally
# DATABASE_URL = os.getenv("DATABASE_URL")

#DATABASE_URI = "sqlite:///C:\\Users\\porte\\Richard_python\\lambda\\lam3\\Twitoff-rich-olson\\twitter_development.db"
SECRET_KEY = os.getenv('SECRET_KEY')




# creating the app the an app factory
def create_app():
    app = Flask(__name__)

    # This is to be able to use flash messaging if we wanted
    app.config["SECRET_KEY"] = SECRET_KEY
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)

    return app








# Will go into here to start to run the module of 
# the application
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
