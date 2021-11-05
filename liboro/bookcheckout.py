"""
BOOK CHECKOUT MODULE
Handles checking out a book from the library.
Makes the neccessary changes to the database file.
By F015011
NOV/DEC 2020
"""

from booksearch import *
from bookweed import *

def checkoutBook(records, b_id, m_id,errorLabel):
    """
    Finds the index of the book by the id given, checks if its available,
    and changes the holder id of the given book to the member id given
    """
    try:
        if b_id.isdigit() and m_id.isdigit():
            book_i = findBookIndexById(records, b_id)
            if availabilityCheck(records,str(b_id))==True:
                records[book_i][5]= m_id
                saveToLogFile(records, b_id)
                errorLabel['text']="Book checked out successfully, press confirm to save."
                print("CHECKOUT SUCCESS.")
            else:
                errorLabel['text']="Sorry, this book is unavailable to checkout."
                print("CHECKOUT ERROR: Book not available for checkout.")
        else:
            errorLabel['text']="Please enter a valid book and member ID."
    except:
        print("BOOK CHECKOUT ERROR")

def availabilityList(records):
    """
    Creates a list of available books by checking all records for a
    "0" at the holder id index, if a 0 is found, the book is added.
    The list containing the book's details is returned.
    """
    try:
        available=False
        availableBooks=[]
        for i in range (0,len(records)):
            if records[i][5]=="0":
                availableBooks.append(records[i])
                available=True
        if available:
            return availableBooks
        else:
            print("Sorry, there are no currently available books.")
    except:
        print("AVAILABILITY LISTING ERROR")

def availabilityTitleList(records,b_title):
    """
    The title of every currently available book is returned.
    """
    try:
        count=0
        available=False
        availableBooks=[]
        books=findBookByTitle(records, b_title)
        for i in range (0,len(books)):
            if books[i][5]=="0":
                availableBooks.append(books[i])
                available=True
                count+=1
        if available:
            return availableBooks
        else:
            print("Sorry, there are no copies available of",b_title)
    except:
        print("AVAILABILITY TITLE LIST ERROR")

#Functions are tested with a try,except clause when they are called. 
