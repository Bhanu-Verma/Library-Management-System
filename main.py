from library import *
from user import *
from book import *

def main():
    library = Library("Shrinivas Deshpandey Library")
    
    user_bhanu = User("Bhanu Verma")
    library.register_user(user=user_bhanu)

    book_hcv = Book("ISOO1", "Concepts of Physics", "H.C. Verma", BookCategory.SCIENCE)
    library.add_book(book_hcv, 10)

    library.issue_book("ISOO1", user_bhanu.user_id)
    library.issue_book("ISOO1", user_bhanu.user_id)

    user_nitin = User("Nitin Verma")
    library.issue_book("ISOO1", user_nitin.user_id)

    library.issue_book("ISOO2", user_bhanu.user_id)

    library.return_book("ISOO1", user_nitin.user_id)
    library.return_book("ISOO2", user_bhanu.user_id)
    library.return_book("ISOO1", user_bhanu.user_id)

    print("\n=================================================================")
    search_type = input("What do you want to search by:\n1. Category\n2. Author\n3. Title\n")
    search_term = input("Enter search term: ")

    retrieved_books = library.search_book(search_type, search_term)
    for (idx, book) in enumerate(retrieved_books):
        print(f"{idx+1}: {book.title}")
    print("=================================================================\n")

if __name__ == "__main__":
    main()