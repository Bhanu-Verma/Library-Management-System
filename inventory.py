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
        print(f"'{book.title}' added successfully.")
        print(f"Total Copies: {self.books[isbn].total_copies}")
        print(f"Available Copies: {self.books[isbn].available_copies}")

    def issue_book(self, book_isbn):
        if book_isbn not in self.books or self.books[book_isbn].available_copies < 1:
            print("Sorry! book is not available right now")
            return False
    
        self.books[book_isbn].available_copies -= 1
        return True
    
    def update_book_return(self, book_isbn):
        if book_isbn not in self.books:
            return
        
        self.books[book_isbn].available_copies += 1

    def get_book_by_isbn(self, book_isbn):
        return self.all_books.get(book_isbn)
    
    def search_by_func(self, func):
        retrieved_books = []
        for (_, book) in self.all_books.items():
            if func(book):
                retrieved_books.append(book)
        return retrieved_books
        
    def search_by_category(self, category):
        return self.search_by_func(lambda x : x.category==category)
    
    def search_by_author(self, author):
        return self.search_by_func(lambda x: x.author==author)
    
    def search_by_title(self, title):
        return self.search_by_func(lambda x: x.title==title)