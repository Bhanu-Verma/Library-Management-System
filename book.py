from enum import Enum
import datetime

class BookCategory(Enum):
    SCIENCE = 1
    LITERATURE = 2
    FICTION = 3
    THESIS = 4
class Book:
    days_in_month = 30

    def __init__(self, isbn, title, author, category):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
