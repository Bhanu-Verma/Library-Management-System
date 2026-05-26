class Inventory:
    class BookCount:
        def __init__(self):
            self.total_copies = 0
            self.available_copies = 0

    def __init__(self):
        self.books = {}
        self.all_books = {}

    def add_book(self, book, quantity):
        isbn = book.isbn
        count = self.books.get(isbn)

        if count is None:
            self.books[isbn] = self.BookCount()
            self.all_books[isbn] = book
        
        self.books[isbn].total_copies += quantity
        self.books[isbn].available_copies += quantity
        print("\n=================================================================")
        print(f"'{book.title}' added successfully.")
        print(f"Total Copies: {self.books[isbn].total_copies}")
        print(f"Available Copies: {self.books[isbn].available_copies}")
        print("=================================================================\n")

    def issue_book(self, book_isbn):
        if book_isbn not in self.books or self.books[book_isbn].available_copies < 1:
            print("Sorry! book is not available right now")
            return False
    
        self.books[book_isbn].available_copies -= 1
        return True

    def get_book_by_isbn(self, book_isbn):
        return self.all_books.get(book_isbn)
        