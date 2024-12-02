from save_contacts import save_all_contacts

def remove_contact(all_contacts):
    phone = input("Enter the phone number of the contact to remove: ").strip()
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return all_contacts

    phone = int(phone)
    for contact in all_contacts:
        if contact['phone'] == phone:
            all_contacts.remove(contact)
            save_all_contacts(all_contacts)
            print("Contact removed successfully!")
            return all_contacts

    print("Contact not found.")
    return all_contacts
