from inventory import *

class Library:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.users = []
        print(f"{name} is now open................")