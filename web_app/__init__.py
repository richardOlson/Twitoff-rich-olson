

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes

# creating the app the an app factory
def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)

    return app








# Will go into here to start to run the module of 
# the application
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
