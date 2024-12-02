import add_contacts
import view_contacts
import save_contacts
import load_contacts
import remove_contacts
import search_contacts

# Load existing contacts from file
all_contacts = load_contacts.load_all_contacts()

def display_menu():
    print("\nWelcome to Contact Book Management System")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Remove a Contact")
    print("4. Search Contacts")
    print("0. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "0":
        print("Exiting the program. Goodbye!")
        break
    elif choice == "1":
        all_contacts = add_contacts.add_contact(all_contacts)
    elif choice == "2":
        view_contacts.view_all_contacts(all_contacts)
    elif choice == "3":
        all_contacts = remove_contacts.remove_contact(all_contacts)
    elif choice == "4":
        search_contacts.search_contact(all_contacts)
    else:
        print("Invalid choice. Please try again.")
