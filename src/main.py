#!/usr/bin/env python3

import datetime
import csv
import os


class Contact:
    def __init__(self, name, phone, email, contact_interval):
        self.name = name
        self.phone = phone
        self.email = email
        self.contact_interval = contact_interval  # in days
        self.last_contact_date = None

    def update_contact_date(self):
        self.last_contact_date = datetime.datetime.now()

    def __str__(self):
        last_contact = (
            self.last_contact_date.strftime("%Y-%m-%d %H:%M:%S")
            if self.last_contact_date
            else "Never"
        )
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Last Contact: {last_contact}"

    def to_csv_row(self):
        last_contact = (
            self.last_contact_date.strftime("%Y-%m-%d %H:%M:%S")
            if self.last_contact_date
            else ""
        )
        return [self.name, self.phone, self.email, last_contact]

    def is_due_for_contact(self):
        if self.last_contact_date is None:
            return True
        due_date = self.last_contact_date + datetime.timedelta(
            days=self.contact_interval
        )
        return datetime.datetime.now() >= due_date


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


def main():
    crm = CRM()

    # List due contacts before showing the menu
    crm.list_due_contacts()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Log Contact")
        print("3. Edit Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_interval = int(
                input(
                    "How often (in days) do you want to get in touch with this person? "
                )
            )
            crm.add_contact(name, phone, email, contact_interval)

        elif choice == "2":
            name = input("Who did you contact?")
            crm.contact_person(name)

        elif choice == "3":
            name = input("Which contact do you want to edit?")
            crm.update_contact(name)

        elif choice == "4":
            crm.list_contacts()

        elif choice == "5":
            print("Exiting CLICRM.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
