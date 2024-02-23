from config import db

# This file is to handle the database models.

""" 
This class represents a contact in the database containing IDs, 
first names, last names, and email addresses.
"""
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    """
    to_json: This method returns a JSON representation of the object.
    Param: None
    Returns: A JSON representation of the object.
    """
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }
    