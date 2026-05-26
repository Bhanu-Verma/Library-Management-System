from inventory import *

class Library:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.users = {}
        print(f"'{name}' is now open................")

    def register_user(self, user):
        self.users[user.user_id] = user
        print(f"'{user.name}' is now registerd in '{self.name}'")

    def add_book(self, book, quantity):
        self.inventory.add_book(book, quantity)
