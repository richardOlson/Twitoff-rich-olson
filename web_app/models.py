# This is the file that will interface with the tweets database

# The table has 2 columns:  user_id |  tweet

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()


class Book(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))



#class tweet(db.Model):
#    user_id = db.Column(db.Integer, primary_key=True)
#    tweet =  db.Column(db.String(128))

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text = db.Column(db.String(500))
    embedding = db.Column(db.PickleType)
    # This is what will
    user = db.relationship("User", backref=db.backref("tweets", lazy=True))