#!/usr/bin/env python3

from contacts import Contact
from crm import CRM
from repl import repl_loop

contact_file = "./data/contacts.csv"
crm = CRM()


def main():
    crm.list_due_contacts()
    repl_loop()


if __name__ == "__main__":
    main()
