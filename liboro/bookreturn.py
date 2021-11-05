"""
RETURN BOOK MODULE
Handles returning a book to the database.
Makes the neccessary changes to the database file.
By Joshua de Bruxelles
NOV/DEC 2020
"""
from booksearch import *

def returnBook(records, b_id, m_id,errorLabel):
    """
    Sets value of the holder id to 0 to indicate that it is
    no longer checked out.
    """
    try:
        if b_id.isdigit() and m_id.isdigit():
            book_i = findBookIndexById(records, b_id)
            if records[book_i][5] == m_id:
                if availabilityCheck(records,str(b_id))==False:
                    records[book_i][5]= "0"
                    errorLabel['text'] = "Book returned - press confirm to save changes."
                else:
                    errorLabel['text'] = "Invalid Book ID - not checked out."
            else:
                errorLabel['text'] ="Invalid Member ID - does not match checked out book"
                print("RETURN ERROR: Member ID match")
        else:
            errorLabel['text'] = "Please enter a valid book and member ID."
    except:
        print("BOOK RETURN ERROR")

#Functions are tested with a try,except clause when they are called. 
