def save_all_contacts(all_contacts):
    with open("contacts.csv", "w") as file:
        for contact in all_contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")
