contacts = []

def display_main_menu():
    print("\nContact Management System")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def display_contact_list():
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def add_contact():
    print("\nAdd New Contact:")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    new_contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(new_contact)
    print("Contact added successfully!")

def search_contact():
    term = input("\nEnter name or phone number to search: ")
    results = [contact for contact in contacts if term.lower() in contact['name'].lower() or term in contact['phone']]
    
    if results:
        print("\nSearch Results:")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['name']} - {result['phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    term = input("\nEnter name or phone number to update: ")
    for contact in contacts:
        if term.lower() in contact['name'].lower() or term in contact['phone']:
            print("\nCurrent Details:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            contact['name'] = input("New Name: ")
            contact['phone'] = input("New Phone: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")
            
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")

def delete_contact():
    term = input("\nEnter name or phone number to delete: ")
    for i, contact in enumerate(contacts):
        if term.lower() in contact['name'].lower() or term in contact['phone']:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")

def main():
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            display_contact_list()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
