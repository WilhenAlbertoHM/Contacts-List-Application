from flask import request, jsonify
from config import app, db
from models import Contact

# This file consists of a CRUD (Create, Read, Update, Delete) API for the backend.

"""
get_contacts: This method returns a list of all contacts in the database.
Param: None
Returns: A JSON representation of the list of contacts.
"""
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = [contact.to_json() for contact in contacts]
    return jsonify({"contacts": json_contacts})

"""
create_contact: This method creates a new contact in the database.
Param: None
Returns: A JSON representation of the new contact.
"""
@app.route("/create_contact", methods=["POST"])
def create_contact():
    # Get the data from the request.
    first_name = request.get_json().get("firstName")
    last_name = request.get_json().get("lastName")
    email = request.get_json().get("email")

    # If any of the fields are missing, return an error.
    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name, and email."}), 400
    
    # Add a new contact to the database; if an error occurs, return the error.
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201

"""
update_contact: This method updates a contact in the database.
Param: user_id: The ID of the contact to update.
Returns: A JSON representation of the updated contact.
"""
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    # Find the contact in the database.
    contact = Contact.query.get(user_id)

    # If the contact does not exist, return an error.
    if not contact:
        return jsonify({"message": "User not found!"}), 404
    
    # Update the contact with the new data.
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    # Commit the changes to the database and return a success message.
    db.session.commit()
    return jsonify({"message": "User updated!"}), 200

"""
delete_contact: This method deletes a contact from the database.
Param: user_id: The ID of the contact to delete.
Returns: A JSON representation of the deleted contact.
"""
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    # Find the contact in the database.
    contact = Contact.query.get(user_id)

    # If the contact does not exist, return an error.
    if not contact:
        return jsonify({"message": "User not found!"}), 404

    # Delete the contact from the database and return a success message.
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()    
    app.run()
