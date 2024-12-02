def load_all_contacts():
    all_contacts = []
    try:
        with open("contacts.csv", "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split(",")
                all_contacts.append({"name": name, "email": email, "phone": int(phone), "address": address})
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh.")
    return all_contacts
