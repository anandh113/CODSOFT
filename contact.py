#TASK 5
contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.")
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print("Name:", name, "| Phone:", details["phone"])
def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["phone"]:
            print("\nContact Found")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            found = True
    if not found:
        print("Contact not found.")
def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input("New phone number: ") or contacts[name]["phone"]
        email = input("New email: ") or contacts[name]["email"]
        address = input("New address: ") or contacts[name]["address"]
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        contacts[name]["address"] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
while True:
    print("\n--- Contact Management Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Management System.")
        break
    else:
        print("Invalid choice. Please try again.")