from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# This file is to handle the configuration of the Flask app and the database.

# Create a Flask app and add CORS support.
app = Flask(__name__)
CORS(app)

# Add database configuration.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create a database object.
db = SQLAlchemy(app)
