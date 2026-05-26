from library import *
from user import *

def main():
    library = Library("Shrinivas Deshpandey Library")
    
    user_bhanu = User("Bhanu Verma")
    library.register_user(user=user_bhanu)

if __name__ == "__main__":
    main()