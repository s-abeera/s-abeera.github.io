import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

config = dotenv_values(".env")

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config['SECRET_KEY'] = config['SECRET_KEY']

from web import routes

