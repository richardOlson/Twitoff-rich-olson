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