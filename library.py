from inventory import *
from book import *
import datetime

class BorrowRecord:
    def __init__(self, user_id, book_isbn, issue_date, return_date):
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.issue_date = issue_date
        self.return_date = return_date


class Library:
    PER_DAY_FINE = 1

    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.users = {}
        self.borrow_records = {}
        print(f"'{name}' is now open................")

    def register_user(self, user):
        self.users[user.user_id] = user
        print(f"'{user.name}' is now registerd in '{self.name}'")

    def user_registered(self, user_id):
        return user_id in self.users
    
    def book_registered(self, book_isbn):
        return self.inventory.get_book_by_isbn(book_isbn) is not None

    def add_book(self, book, quantity):
        self.inventory.add_book(book, quantity)

    def has_issued(self, user_id, book_isbn):
        if user_id not in self.borrow_records:
            return False
        
        for record in self.borrow_records[user_id]:
            if record.book_isbn == book_isbn:
                return True
        
        return False
    
    def get_return_date(self, book, issue_date):
        match book.category:
            case BookCategory.SCIENCE:
                return issue_date + datetime.timedelta(days=Book.days_in_month*3)
            case BookCategory.LITERATURE:
                return issue_date + datetime.timedelta(month=Book.days_in_month*2)
            case BookCategory.FICTION:
                return issue_date + datetime.timedelta(month=Book.days_in_month*2)
            case BookCategory.THESIS:
                return issue_date + datetime.timedelta(month=Book.days_in_month*5)
    

    def issue_book(self, book_isbn, user_id):
        # Ensure that user is registered
        if not self.user_registered(user_id):
            print(f"User Id: '{user_id}' is not registered in {self.name}")
            return
        
        user = self.users[user_id]
        book = self.inventory.get_book_by_isbn(book_isbn)

        if book is None:
            print(f"Sorry! book is not available.")
            return

        # Ensure that user hasn't previously issued the same book
        if self.has_issued(user_id, book_isbn):
            print(f"User: '{user.name}' has already issued the book '{book.title}'.")
            return
        
        status = self.inventory.issue_book(book_isbn)
        
        if status:
            if user_id not in self.borrow_records:
                self.borrow_records[user_id] = []

            issue_date = datetime.datetime.now()
            return_date = self.get_return_date(book, issue_date)

            self.borrow_records[user_id].append(
                BorrowRecord(user_id, 
                            book_isbn, 
                            issue_date,
                            return_date
                        )
            )
            print("\n=================================================================")
            print(f"Book '{book.title}' issued successfully to '{user.name}'")
            print(f"Issue Date: {issue_date.strftime('%A, %d %B %G')}")
            print(f"Return Date: {return_date.strftime('%A, %d %B %G')}")
            print("=================================================================\n")



    def return_book(self, book_isbn, user_id):
        if not self.user_registered(user_id):
            print(f"User Id: '{user_id}' is not registered in {self.name}")
            return 
        
        if not self.book_registered(book_isbn):
            print(f"Book ISBN: '{book_isbn}' is not registered in {self.name}")
            return

        user = self.users[user_id]
        book = self.inventory.get_book_by_isbn(book_isbn)
        
        if not self.has_issued(user_id, book_isbn):
            print(f"User: '{user.name}' hasn't issued the book '{book.title}'.")
            return
    
        print("\n=================================================================")

        borrow_record = None
        for record in self.borrow_records[user_id]:
            if record.book_isbn == book_isbn:
                borrow_record = record
                break
        
        return_date = borrow_record.return_date
        current_date = datetime.datetime.now()
        if return_date.date() < current_date.date():
            fine = (current_date.date() - return_date.date()) * Library.PER_DAY_FINE
            fine_submitted = input(f"Fine of Rs.{fine} submitted?(yes/no): ")
            if fine_submitted == "no":
                print("Please submit the fine first")
                print("=================================================================\n")
                return

        self.borrow_records[user_id].remove(borrow_record)
        self.inventory.update_book_return(book_isbn)

        print(f"Book '{book.title}' successfully returned by '{user.name}'")
        print("=================================================================\n")

    def search_book(self, search_type, search_term):
        if search_type == "Category":
            return self.inventory.search_by_category(search_term)
        if search_type == "Author":
            return self.inventory.search_by_author(search_term)
        if search_type == "Title":
            return self.inventory.search_by_title(search_term)