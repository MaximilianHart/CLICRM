#!/usr/bin/env python3

import datetime


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
