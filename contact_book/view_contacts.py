def view_all_contacts(all_contacts):
    if not all_contacts:
        print("No contacts found.")
        return
    print("\nAll Contacts:")
    print("-" * 40)
    for i, contact in enumerate(all_contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    print("-" * 40)
