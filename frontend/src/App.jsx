import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import "./App.css";

function App() {
  // Create state variables.
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState({});

  // As soon as the page loads, fetch the contacts from the server.
  useEffect(() => {
    fetchContacts();
  }, []);

  // Fetch the contacts from the Flask server server.
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts");
    const data = await response.json();
    setContacts(data.contacts);
  };

  // Function to open the create modal; box to fill in contact information.
  const openCreateModal = () => {
    if (!isModalOpen) {
      setIsModalOpen(true);
    }
  };

  // Function to close the modal.
  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact({});
  };

  // Function to open the edit modal.
  const openEditModal = (contact) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  // Callback function to update the contact list.
  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <>
      <ContactList
        contacts={contacts}
        updateContact={openEditModal}
        updateCallback={onUpdate}
      />
      <button onClick={openCreateModal}>Create New Contact</button>

      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <ContactForm
              existingContact={currentContact}
              updateCallback={onUpdate}
            />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
