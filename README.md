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