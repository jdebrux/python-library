"""
BOOK WEEDING DATA MODULE
Calculates popularity of each book in the library based on number of checkouts
found in the log file.
By F015011
NOV/DEC 2020
"""
from booksearch import *

def getLogRecords():
    """Reads data from log file."""
    try:
        logs=[]
        f=open("logfile.txt","r")
        for line in f:
            s=line.strip()
            log=s.split("|")
            logs.append(log)
        f.close()
        return logs
    except:
        print("ERROR GETTING LOG RECORDS")

def saveToLogFile(records, b_id):
    """
    Saves data to log file.
    The same format is used as the database module in order to allow reuse of
    searching functions.
    """
    try:
        book = findBookById(records, b_id)
        f=open("logfile.txt","a")
        line = '|'.join([str(i) for i in book])
        f.write("%s\n"%line)
        f.close()
    except:
        print("ERROR SAVING TO LOG FILE")

def countBooks(logs,b_title):
    """Counts the number of occurrences of a given book title"""
    try:
        books=findBookByTitle(logs,b_title)
        checkoutSum = len(books)
        return checkoutSum
    except:
        print("ERROR COUNTING BOOKS")
    
def getBookTitles(logs):
    """Creates a list of each unique book title found in the log file."""
    try:
        bookTitles = []
        for log in logs:
            bookTitles.append(log[2])
        bookTitles = set(bookTitles)
        return list(bookTitles)
    except:
        print("ERROR GETTING BOOK TITLES")

def getTotals(logs):
    """Creates a list of total checkouts for each title in the log file."""
    try:
        totals=[]
        bookTitles = getBookTitles(logs)
        for title in bookTitles:
            totals.append(countBooks(logs,title))
        return totals
    except:
        print("ERROR GETTING TOTAL CHECKOUTS")

def formatData(logs,lstInfo,popLbl,unpopLbl):
    """
    Formats the data for the weeding file into the list box as well as
    displaying the least and most popular books.
    """
    try:
        titles = getBookTitles(logs)
        totals = getTotals(logs)
        info = list(zip(totals,titles))
        sorted_info = sorted(info,key=lambda x: x[0])#sorts data by first element in each tuple
        #place data in list box
        i=2
        lstInfo.delete(0,'end')
        lstInfo.insert(1, "TOTAL CHECKOUTS | BOOK TITLE")
        for item in sorted_info:
            line=' | '.join([str(j) for j in item])
            lstInfo.insert(i,line)
            i+=1

        #sort data by total
        popular = sorted_info[-1]
        unpopular = sorted_info[0]
        popLbl['text'] = "The most popular book is %s"%popular[1]
        unpopLbl['text'] = "The least popular book is %s"%unpopular[1]
    except:
        print("WEEDING DATA FORMAT ERROR")


#Functions are tested with a try,except clause when they are called. 
