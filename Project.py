import re

def add_contact(contacts):
        phone_pattern = re.compile("^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$")
        email_pattern = re.compile("^\S+@\S+\.\S+$")
        while True:    
            details = input("Enter phone number")
            if details in contacts:
                print('The contact already exists!')
                continue
            if not phone_pattern.search(details):
                print("Enter a valid phone number")
                continue
            name = input("Enter contacts name")
            number = input("Enter phone number")
            if not phone_pattern.search(number):
                print("Enter a valid phone number")
                continue
            email = input("Enter email address here")
            if not email_pattern.search(email):
                print("Enter a valid email")
                continue
            
            new_contact = {'Name': name, 'Phone Number' : number, 'Email': email}
            contacts[details] = new_contact
            return contacts

def edit_contact(contacts):
    phone_pattern = re.compile("^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$")
    email_pattern = re.compile("^\S+@\S+\.\S+$")
    while True:
        contact = input("Enter the number of the contact you wish to edit")
        if not phone_pattern.match(contact):
            print("Enter a valid phone number")
            continue
        if contact in contacts:
            edit = input("What would you like to edit? Name, Phone Number, or Email").lower()
            if edit == 'name':
                updated_name = input("What would you like to change the contact name to?")
                contacts[contact]['Name'] = updated_name

            elif edit == 'phone number':
                updated_number = input("What would you like to change the contact number to?")
                if not phone_pattern.match(updated_number):
                    print("Enter a valid phone number")
                    continue
                contacts[contact]['Phone Number'] = updated_number
                contacts[updated_number] = contacts.pop(contact)

            elif edit == 'email':
                updated_email = input("What would you like to change the contact email to?")
                if not email_pattern.match(updated_email):
                    print("Enter a valid email address")
                    continue
                contacts[contact]['Email'] = updated_email
        else:
            print("Contact not found")

        more_edits = input("Would you like to edit any other information? (Yes/No)").lower()
        if more_edits == "yes":
            continue
        else:
            break
    
    return contacts 

def delete_contact(contacts):
    phone_pattern = re.compile("^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$")
    while True:
        contact = input("Enter the number of the contact you wish to delete")
        if not phone_pattern.match(contact):
                print("Enter a valid phone number")
                continue
        if contact in contacts:
            del contacts[contact]
            print(f'The contact under the number {contact} has been deleted')
            return contact

def search_contacts(contacts):
    phone_pattern = re.compile("^\d{3}[-.\s]?\d{3}[-.\s]?\d{4}$")
    while True:
        contact = input("Enter the number of the contact you wish to search for")
        if not phone_pattern.match(contact):
            print("Enter a valid number")
            continue
        contact_details = contacts.get(contact)
        if contact_details:
            print(f"\n{contact}" + ":")
            print(f"\tName: {contact_details['Name']}")
            print(f"\tPhone Number: {contact}")
            print(f"\tEmail: {contact_details['Email']}\n")
            return contact
    
def display_contacts(contacts):
    for contact, info in contacts.items():
        print(contact)
        name = info.get('Name', 'N/A')
        number = info.get('Phone Number', 'N/A')
        email = info.get('Email', 'N/A')
        print(f' Name: {name}\n Phone Number: {number}\n Email: {email}\n')

def export_contacts(contacts):
    with open('contacts.txt', 'w') as file:
        for contact, info in contacts.items():
            name = info.get('Name', 'N/A')
            number = info.get('Phone Number', 'N/A')
            email = info.get('Email', 'N/A')
            file.write(f'{contact}\n\t Name: {name}\n\t Phone Number: {number}\n\t Email: {email}\n')
        print("Contacts successfully exported!")



contact_details = {'213-345-6574': {'Name' : 'Alice', 'Phone Number' : '213-345-6574', 'Email' : 'alice@gmail.com'}}
                   
while True:
    menu = input("Welcome to the Contact Management System! \nMenu:\n1. Add a new contact \n2. Edit an existing contact \n3. Delete a contact \n4. Search for a contact \n5. Display all contacts \n6. Export contacts to a text file \n7. Quit\n")
    if menu == '1':
        add_contact(contact_details)
    elif menu == '2':
        edit_contact(contact_details)
    elif menu == '3':
        delete_contact(contact_details)
    elif menu == '4':
        search_contacts(contact_details)
    elif menu == '5':
        display_contacts(contact_details)
    elif menu == '6':
        export_contacts(contact_details)
    elif menu == '7':
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option")