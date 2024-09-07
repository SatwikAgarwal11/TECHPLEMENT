# Initialize an empty list to store contacts
contacts = []

# Function to validate phone number
def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 9 and len(phone) <= 13

# Function to add a contact
def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    phone = input("Enter phone number: ").strip()
    if not validate_phone(phone):
        print("Error: Phone number must be digits only and between 9 to 13 characters long.")
        return
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Error: A contact with this name already exists.")
            return
    
    contacts.append({'name': name, 'phone': phone})
    print("Contact added successfully.")

# Function to search for a contact by name
def search_contact():
    name = input("Enter name to search: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            return
    print("Contact not found.")

# Function to update an existing contact
def update_contact():
    name = input("Enter name of the contact to update: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_phone = input("Enter new phone number: ").strip()
            if not validate_phone(new_phone):
                print("Error: Phone number must be digits only and between 9 to 13 characters long.")
                return
            contact['phone'] = new_phone
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Main loop to show options and take user input
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()