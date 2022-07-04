# import modles
from models import (Base, session, Book, engine)
# main menu - add, search, analysis, exit, view
# add books to the DB function
# edit books function
# delete books function
# search function
# data cleaning function
# loop runs program


if __name__ == '__main__':
    Base.metadata.create_all(engine)