#!/usr/bin/env python3

import os
from contacts import Contact


class CRM:
    def __init__(self):
        self.contacts = {}
        self.csv_file_path = "./data/contacts.csv"
        self.ensure_data_directory()

    def ensure_data_directory(self):
        os.makedirs(os.path.dirname(self.csv_file_path), exist_ok=True)

    def add_contact(self, name, phone, email, contact_interval):
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        elif phone in self.contacts:
            print(f"Contact with phone {phone} already exists.")
        elif email in self.contacts:
            print(f"Contact with email {email} already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email, contact_interval)
            print(f"Contact {name} added.")
            self.save_to_csv()

    def contact_person(self, name):
        if name in self.contacts:
            self.contacts[name].update_contact_date()
            print(f"Updated last contact date for {name}.")
            self.save_to_csv()
        else:
            print(f"No contact found with name {name}.")

    def update_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Updating contact: {contact}")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            contact_interval = input(
                "Enter new desired contact interval in days (leave blank to keep current): "
            )

            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if contact_interval:
                contact.contact_interval = int(contact_interval)

            self.save_to_csv()
            print(f"Contact {name} updated.")
        else:
            print(f"No contact found with name {name}.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)

    def save_to_csv(self):
        with open(self.csv_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Last Contact"])
            for contact in self.contacts.values():
                writer.writerow(contact.to_csv_row())
        print(f"Contacts saved to {self.csv_file_path}.")

    def list_due_contacts(self):
        due_contacts = [
            contact
            for contact in self.contacts.values()
            if contact.is_due_for_contact()
        ]
        if due_contacts:
            print("\nContacts due for contact:")
            for contact in due_contacts:
                print(contact)
        else:
            print("\nNo contacts are due for contact.")
