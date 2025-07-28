#!/usr/bin/env python3

import os
from crm import CRM


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def quit_program():
    exit(0)


def repl_loop():
    clear_screen()

    while True:
        crm = CRM()

        crm.list_due_contacts()

        while True:
            print("\n=== CLI CRM ===")
            print("1. Add Contact")
            print("2. Log Contact")
            print("3. Edit Contact")
            print("4. List All Contacts")
            print("5. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                contact_interval = int(
                    input(
                        "How often (in days) do you want to get in touch with this person?"
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
