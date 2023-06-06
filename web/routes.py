from flask import Flask, render_template, request, redirect, url_for, g, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

import requests

# Initialize the app

try:
    from web import app
except ImportError:
    from __init__ import app

@app.route('/')
def index():
    '''
    This function is used to render the landing page 
    '''
    return render_template('index.html')

