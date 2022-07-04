# import modles
from models import (Base, session, Book, engine)
# main menu - add, search, analysis, exit, view
def menu():
    while True:
        print('''
              \nProgramming Books
              \r1) Add Book
              \r2) View all books
              \r3) Search for book
              \r4) Book Analysis
              \r5) Exit
              ''')
        choice = input('What would you like to do? ')
        if choice in ('1','2','3','4','5'):
            return choice
        else:
            input('''
                  \rPlease choose one of the options above.
                  \rA number from 1-5.
                  \rPress enter to try again
                  ''')
# add books to the DB function
# edit books function
# delete books function
# search function
# data cleaning function
# loop runs program

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('Goodbye')
            app_running=False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()