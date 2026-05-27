from library import *
from user import *
from book import *

def show_menu():
    print("What do you want to do? (Numeric Input only e.g. 2 for Add Book)")
    print("1. Register User")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

def register_user_flow(lib):
    try:
        name = input("Enter your name: ")
    except:
        print("Try Again!")
        return

    user = User(name)
    lib.register_user(user)

    print(f"Your user id: {user.user_id}")

def add_book_flow(lib):
    try:
        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        category_input = input("Enter Category: ")
        author = input("Enter Author: ")
    except:
        print("Try Again!")
        return

    category = None
    try:
        category = BookCategory[category_input.upper()]
    except KeyError:
        print(f"Enter a valid category")
        return
    
    book = Book(isbn, title, author, category)
    quantity = int(input("Enter quantity: "))

    lib.add_book(book, quantity)

def issue_book_flow(lib):
    try:
        user_id = int(input("Enter your user id: "))
        book_isbn = input("Enter ISBN shown on the book: ")
    except:
        print("Try Again!")
        return

    lib.issue_book(book_isbn, user_id)

def return_book_flow(lib):
    try:
        user_id = int(input("Enter your user id: "))
        book_isbn = input("Enter ISBN shown on the book: ")
    except:
        print("Try Again!")
        return

    lib.return_book(book_isbn, user_id)

def search_book_flow(lib):
    try:
        search_type_input = input("What do you want to search by:\n1. Category\n2. Author\n3. Title\n")
        search_term = input("Enter search term: ")
    except:
        print("Try Again!")
        return

    search_type = None
    if search_type_input == "1" or search_type_input == "Category":
        search_type = "Category"
    if search_type_input == "2" or search_type_input == "Author":
        search_type = "Author"
    if search_type_input == "3" or search_type_input == "Title":
        search_type = "Title"

    if search_type == "Category":
        try:
            search_term = BookCategory[search_term.upper()]
        except KeyError:
            print(f"Enter a valid category")
            return

    retrieved_books = lib.search_book(search_type, search_term)
    
    if retrieved_books is None or retrieved_books == []:
        print("No Book found!")
        return
    
    print("Here are the books based on your search: ")
    for book in retrieved_books:
        print("")
        print(f"{book}")    

def main():
    library = Library("Shrinivas Deshpandey Library")
    
    while True:
        print("\n=================================================================")
        show_menu()
        choice = input()

        match choice:
            case "1": 
                register_user_flow(library)
                pass

            case "2":
                add_book_flow(library)
                pass

            case "3":
                issue_book_flow(library)
                pass

            case "4":
                return_book_flow(library)
                pass

            case "5":
                search_book_flow(library)
                pass

            case "6":
                break

            case _:
                print("Not a valid input")
                pass

if __name__ == "__main__":
    main()