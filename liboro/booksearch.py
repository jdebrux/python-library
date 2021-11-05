"""
BOOK SEARCH MODULE
Handles the searching of data from the database text file.
Also handles displaying the data found to the user.
By F015011
NOV/DEC 2020
"""

def showBookById(records, b_id,lstBooks,errorLabel):
    """
    Searches database for given ID, inserts to list box if found.
    """
    try:
        found=False
        if b_id.isdigit():
            lstBooks.delete(0,'end')
            lstBooks.insert(1, " ID | ISBN | TITLE | AUTHOR | DATE | HOLDER ID")
            for record in records:
                if record[0]==b_id:
                    line='|'.join([str(j) for j in record])
                    lstBooks.insert(1,line)
                    found=True
        if found:
            errorLabel['text']= "Found successfully..."
        else:
            errorLabel['text']="Please enter a valid Book ID."
    except:
        print("ERROR SHOWING BOOK BY ID")

def showBookByTitle(records, b_title,lstBooks,errorLabel):
    """
    Searches database for given title, inserts to list box if found.
    """
    try:
        i=2
        found=False
        lstBooks.delete(0,'end')
        lstBooks.insert(1, "ID|ISBN|TITLE|AUTHOR|DATE|HOLDER ID")
        for record in records:
            if b_title in record[2]:
                line='|'.join([str(j) for j in record])
                lstBooks.insert(i,line)
                i+=1
                found=True
        if found:
            errorLabel['text']="Found successfully..."
        else:
            errorLabel['text']= "Sorry, this book is not in the system."
    except:
        print("ERROR SHOWING BOOK TITLES")

def showBookByISBN(records,b_isbn,lstBooks,errorLabel):
    """
    Searches database for given ISBN, inserts to list box if found.
    """
    try:
        found=False
        if b_isbn.isdigit():
            lstBooks.delete(0,'end')
            lstBooks.insert(1, "ID|ISBN|TITLE|AUTHOR|DATE|HOLDER ID")
            for record in records:
                if record[1]==b_isbn:
                    line='|'.join([str(j) for j in record])
                    lstBooks.insert(1,line)
                    found=True
            if found:
                errorLabel['text']="Found successfully..."
            else:
                errorLabel['text']= "Sorry, this book is not in the system."
        else:
            errorLabel['text']="Please enter a valid ISBN."
    except:
        print("ERROR SHOWING BOOK BY ISBN")

def showBookByAuthor(records, b_auth,lstBooks,errorLabel):
    """
    Searches database for given Author, inserts to list box if found.
    """
    try:
        found=False
        lstBooks.delete(0,'end')
        lstBooks.insert(1, "ID|ISBN|TITLE|AUTHOR|DATE|HOLDER ID")
        for record in records:
            if b_auth in record[3]:
                line='|'.join([str(j) for j in record])
                lstBooks.insert(1,line)
                found=True
        if found:
            errorLabel['text']="Found successfully..."
        else:
            errorLabel['text']="Sorry, there are no books by this author in the system."
    except:
        print("ERROR SHOWING BOOK BY AUTHOR")
    
def findBookByTitle(records, b_title):
    """
    Searches for given book title in database, returns as list if found.
    """
    try:
        books=[]
        found=False
        for i in range(0,len(records)):
            if b_title in records[i][2]:
                books.append(records[i])
                found=True
        if found:
            return books
        else:
            return "TITLE SEARCH ERROR: Book Title given is not in the system."
    except:
        print("ERROR FINDING BOOK BY TITLE")

def findBookById(records,b_id):
    """
    Searches for given book id in database, returns as list if found.
    """
    try:
        for record in records:
            if record[0]==b_id:
                return record
        return "ID SEARCH ERROR: ID gicen is not in the system."
    except:
        print("ERROR FINDING BOOK BY ID")

def findBookIndexById(records,b_id):
    """
    Uses book id search to return the index of a given book.
    """
    try:
        book=findBookById(records, b_id)
        return records.index(book)
    except:
        print("ERROR FINDING BOOK BY ID")

def availabilityCheck(records, b_id):
    """
    Checks the value of the holder id to see if a given book is available or not.
    """
    try:
        count=0
        book=findBookById(records, b_id)
        if book[5]=="0":
            return True
        else:
            return False
    except:
        print("AVAILABILITY CHECK ERROR")

#Functions are tested with a try,except clause when they are called. 
