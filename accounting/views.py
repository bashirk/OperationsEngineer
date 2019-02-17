# You will probably need more methods from flask but this one is a good start.
from flask import render_template, jsonify, json, Response

# Import things from Flask that we need.
from accounting import app, db

# Import our models
from models import Contact, Invoice, Policy, Payment
from datetime import datetime, date

 # Import for SQL exception
import sqlalchemy

# Routing for the server.
@app.route("/")
def index():
    # You will need to serve something up here.
    return render_template('index.html')
