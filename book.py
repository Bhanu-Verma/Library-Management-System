from enum import Enum

class BookCategory(Enum):
    SCIENCE = 1
    LITERATURE = 2
    FICTION = 3
    THESIS = 4
class Book:
    def __init__(self, isbn, title, author, category):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category

    