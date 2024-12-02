def search_contact(all_contacts):
    query = input("Enter name, email, or phone to search: ").strip().lower()
    results = [contact for contact in all_contacts if query in str(contact.values()).lower()]

    if not results:
        print("No matching contacts found.")
    else:
        print("\nSearch Results:")
        print("-" * 40)
        for i, contact in enumerate(results, start=1):
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
        print("-" * 40)
