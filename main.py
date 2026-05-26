from library import *
from user import *
from book import *

def main():
    library = Library("Shrinivas Deshpandey Library")
    
    user_bhanu = User("Bhanu Verma")
    library.register_user(user=user_bhanu)

    book_hcv = Book("ISOO1", "Concepts of Physics", "H.C. Verma", BookCategory.SCIENCE)
    library.add_book(book_hcv, 10)

if __name__ == "__main__":
    main()