# Twitoff-rich-olson
Repository for the Twitoff app


## Instalation

To use this you can clone this Repo on to your
local computer

## Setup

Set up a pipenv environment and then install the 
following packages:
    pipenv install Flask Flask_SQLAlchemy Flask-Migrate

## Usage

'''sh
# Mac:
FLASK_APP=hello.py flask run

# Windows:
export FLASK_APP=hello.py   
flask run

# Windows alternatively:
set FLASK_APP=web_app
flask run

'''
# How to set up a database
'''sh
FLASK_APP=web_app flask db init 


FLASK_APP=web_app flask db migrate(with 
FLASK_APP=web_app flask db upgrade 
'''

To run locally there is a portion in the __init__.py file that needs
to be uncommented to allow the database to use the sqlite, (local)
database. It is set up to work on different computers that may have 
different file structures.  Some code needs to be commented out that will look for an environment variable (used for when in production on a server.)

Also in the admin_routes a change was made taking the api key from the .env to into the file itself
for production.