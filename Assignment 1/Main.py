import re
import csv
import os
from datetime import datetime


# Utility functions for validation
def validate_phone(phone):
    return re.match(r'\(\d{3}\) \d{3}-\d{4}', phone)


def validate_email(email):
    if email:
        return re.match(r'[^@]+@[^@]+\.[^@]+', email)
    return True  # Optional email


# Contact class with additional display method
class Contact:
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def display(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"  Phone: {self.phone_number}")
        if self.email:
            print(f"  Email: {self.email}")
        if self.address:
            print(f"  Address: {self.address}")
        print(f"  Created At: {self.created_at}")
        print(f"  Last Updated: {self.updated_at}\n")

    def update(self, first_name, last_name, phone_number, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.updated_at = datetime.now()


# PhoneBook class that manages contacts and file persistence
class PhoneBook:
    def __init__(self):
        self.contacts = []

    # Loading the contacts from a CSV file
    def load_contacts_from_csv(self, file_path):
        file_path= "C:\Vibhu Puri\Masters\Fullstack\Assignment 1\contacts.csv"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_contact(row['First Name'], row['Last Name'], row['Phone Number'], row.get('Email'), row.get('Address'))
            print("Contacts loaded from CSV successfully.")
        else:
            print("CSV file not found.")
    
    # Exportinng contatcts to a csv file

    # def save_contacts_to_csv(self, file_path):
    #     with open(file_path, 'w', newline='') as file:
    #         writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name', 'Phone Number', 'Email', 'Address'])
    #         writer.writeheader()
    #         for contact in self.contacts:
    #             writer.writerow({
    #                 'First Name': contact.first_name,
    #                 'Last Name': contact.last_name,
    #                 'Phone Number': contact.phone_number,
    #                 'Email': contact.email,
    #                 'Address': contact.address
    #             })
    #     print("Contacts saved to CSV successfully.")

    # ADDing contacts Manually to the phonebook

    def add_contact(self, first_name, last_name, phone_number, email=None, address=None):
        if not validate_phone(phone_number):
            print("Invalid phone number format.")
            return

        if not validate_email(email):
            print("Invalid email format.")
            return

        new_contact = Contact(first_name, last_name, phone_number, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    # Display the contacts in the phonebook

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        for contact in self.contacts:
            contact.display()

    # Search for contacts in the phonebook

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.first_name.lower() or query.lower() in contact.last_name.lower()]
        if not results:
            print("No contacts found.")
        for contact in results:
            contact.display()

    # group contacts by first name
    def group_contacts_by_first_name(self):
        #Groups contacts alphabetically by the initial letter of their last names.
        grouped = {}
        for contact in self.contacts:  # Group contacts by the first letter of their last name
            first_letter = contact.first_name[0].upper()
            grouped.setdefault(first_letter, []).append(contact)
        for letter, group in grouped.items():  # Print each group of contacts
            print(f"\nContacts starting with {letter}:")
            for contact in group:
                Contact.display(contact)


    # group contacts by Last name
    def group_contacts_by_last_name(self):
        #Groups contacts alphabetically by the initial letter of their last names.
        grouped = {}
        for contact in self.contacts:  # Group contacts by the first letter of their last name
            first_letter = contact.last_name[0].upper()
            grouped.setdefault(first_letter, []).append(contact)
        for letter, group in grouped.items():  # Print each group of contacts
            print(f"\nContacts starting with {letter}:")
            for contact in group:
                Contact.display(contact)

    # Sort contacts by First/last Name
    def sort_contacts(self, by="first_name"):
        #Sorts the contacts by the specified field (first_name or last_name).
        self.contacts = sorted(self.contacts, key=lambda x: getattr(x, by))  # Sort the contacts based on the given field
        print(f"Contacts sorted by {by}:")
        self.display_all_contacts()  # Display the sorted contacts

    # deleting the contacts from the phonebook

    def delete_contact(self, first_name, last_name):
        found = False
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")

    # Updating a contact

    def update_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                print(f"Updating contact: {first_name} {last_name}")
                new_first_name = input("Enter new first name: ")
                new_last_name = input("Enter new last name: ")
                new_phone_number = input("Enter new phone number (###) ###-####: ")
                new_email = input("Enter new email (optional): ")
                new_address = input("Enter new address (optional): ")
                contact.update(new_first_name, new_last_name, new_phone_number, new_email, new_address)
                print("Contact updated successfully.")
                return
        print("Contact not found.")




# Command-line interface for PhoneBook application
def phonebook_cli():
    phonebook = PhoneBook()

    # # Get the current file path
    # current_file_path = os.getcwd()

    # csv_file = str(current_file_path)+'\contacts.csv'

    while True:
        print("\nPhoneBook Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Load Contacts from CSV")
        print("7. Group Contacts by First Name")
        print("8. Group Contacts by Last Name")
        print("9. Sort Contacts by First Name")

        # print("7. Save Contacts to CSV")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number (###) ###-####: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            phonebook.add_contact(first_name, last_name, phone_number, email, address)

        elif choice == '2':
            phonebook.display_all_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            phonebook.search_contacts(query)

        elif choice == '4':
            first_name = input("Enter first name of contact to update: ")
            last_name = input("Enter last name of contact to update: ")
            phonebook.update_contact(first_name, last_name)

        elif choice == '5':
            first_name = input("Enter first name of contact to delete: ")
            last_name = input("Enter last name of contact to delete: ")
            phonebook.delete_contact(first_name, last_name)

        elif choice == '6':
            file_path = input("Enter CSV file path: ")
            phonebook.load_contacts_from_csv(file_path)

        elif choice == '7':
            # Group contacts by the first letter of the First name
            phonebook.group_contacts_by_first_name()
        
        elif choice == '8':
            # Group contacts by the first letter of the last name
            phonebook.group_contacts_by_last_name()

        elif choice == '9':
            # Sort contacts by first or last name
            by = input("Sort by (first_name/last_name): ")
            phonebook.sort_contacts(by)

        # elif choice == '7':
        #     phonebook.save_contacts_to_csv(csv_file)

        elif choice == '11':
            print("Exiting PhoneBook. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    phonebook_cli()