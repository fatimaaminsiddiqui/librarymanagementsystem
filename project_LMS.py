from datetime import date, timedelta
class Book:
    def __init__(self):
        print("Hello")
    def __init__(self, title, author, ISBN,returnDate = None):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.returnDate = returnDate
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'{self.title} by {self.author} has been borrowed.')
        else:
            print(f'{self.title} by {self.author} is not available.')

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f'{self.title} by {self.author} has been returned.')
        else:
            print(f'{self.title} by {self.author} was not borrowed.')

class Library:
    def __init__(self):
        self.books = []
        self.borrowedBooks = []

    def add_borrowedBook(self, borrowedBook):
        self.borrowedBooks.append(borrowedBook)

    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} by {book.author} has been added to the library.')

    def borrow_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                book.borrow()
                return
        print('Book not found.')

    def return_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                book.return_book()
                return
        print('Book not found.')
#Example 
library = Library()
def addBook():
    title= input("Write the title of the book: ")
    print(f'The title of your book is {title}.')
    author= input("Write the author of the book: ")
    print(f'The author of your book is {author}.')
    isbn= int(input("Write the ISBN of the book: "))
    print(f'The ISBN of your book is {isbn}.')
    book = Book(title, author, '9988888')
    library.add_book(book)
    print(f"Your book {book.title} has been added.")
    _menu= input("Do you want to add another book? Type YES to add, type NO to go back to menu")
    if _menu == 'YES'or _menu == 'yes' :
       addBook()
    else:
        menu()
def searchBook():
    searchedBook = Book('','',0)
    book= input("Please enter the name of the book you want to search: ")
    for _book in library.books:
        if _book.title == book:
            searchedBook = _book
            break
    if searchedBook.title == '':
        print("No book found")
    else:
        print("Following are the details of your searched book: /n")
        print(f"TITLE: {searchedBook.title}")
        print(f"AUTHOR: {searchedBook.author}")
        print(f"ISBN: {searchedBook.ISBN}")
    _menu= input("Do you want to search another book? Type YES to add, type NO to go back to menu")
    if _menu == 'YES'or _menu == 'yes' :
       searchBook()
    else:
        menu()
def findBook(book):
     searchedBook = Book('','',0)
     for _book in library.books:
        if _book.title == book:
            searchedBook = _book
            break
     return searchedBook
def borrowBook():
    searchedBook = Book('','',0)
    name= input("Enter your name: ")
    roll_no= input("Enter your roll no: ")
    b_name= input("PLease enter the name of that book you have to borrow: ")
    searchedBook = findBook(b_name)
    if searchedBook.title == '':
        print("The book you want to borrow is not available")
    else:
        returnDate= date.today() + timedelta(days =7)
        searchedBook.returnDate = returnDate
        library.add_borrowedBook(searchedBook) 
        print(f"You have to return this book after 7 days from today which is {returnDate}")
    _menu= input("Do you want to borrow another book? Type YES to borrow, type NO to go back to menu")
    if _menu == 'YES'or _menu == 'yes' :
       borrowBook()
    else:
        menu()    
def returnBook():
    searchedBook = Book('','',0)
    returnedBook= input("Enter the name of the book you want to return: ")
    for _book in library.borrowedBooks:
        if _book.title == returnedBook:
            searchedBook = _book
            break
    if searchedBook.title == '':
        print(f"Please enter the correct name of the book to return")
    else:
        if date.today() > searchedBook.returnDate:
            print("Sorry you are late, you need to give a fine of 500Rs")
        else:
            print("Book return on time, no fine applicable")
    _menu= input("Do you want to return another book? Type YES to return, type NO to go back to menu")
    if _menu == 'YES'or _menu == 'yes' :
       returnBook()
    else:
        menu()       
def menu():
    print("##################### WELCOME TO THE LIBRARY #####################")
    
    print("1- ADD BOOK ")
    print("2- SEARCH BOOK ")
    print("3- BORROW BOOK ")
    print("4- RETURN BOOK ")
    x=int(input("Enter respective number to perform following action: "))
    if x == 1 : 
       addBook() 
    elif x == 2:
        searchBook()
    elif x == 3:
        borrowBook()
    else:
        returnBook()
menu()
