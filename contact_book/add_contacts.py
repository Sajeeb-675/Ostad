from save_contacts import save_all_contacts

def add_contact(all_contacts):
    try:
        name = input("Enter contact's name: ").strip()
        if not name.isalpha():
            raise ValueError("Name must only contain alphabetic characters.")

        email = input("Enter contact's email: ").strip()
        phone = input("Enter contact's phone number: ").strip()
        if not phone.isdigit():
            raise ValueError("Phone number must be numeric.")
        phone = int(phone)

        # Prevent duplicate phone numbers
        for contact in all_contacts:
            if contact['phone'] == phone:
                print("Error: Phone number already exists.")
                return all_contacts

        address = input("Enter contact's address: ").strip()

        contact = {"name": name, "email": email, "phone": phone, "address": address}
        all_contacts.append(contact)
        save_all_contacts(all_contacts)

        print("Contact added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    return all_contacts
