"""
(MAIN) MENU MODULE
Creates the GUI with tkinter using frames.
Calls all neccessary functions required for the program to operate.
Imports the 'liboro' package containing all other modules.
Handles the Graph construction and display with matplotlib.
By F015011
NOV/DEC 2020
"""
#imports
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
try:
    from Tkinter import * #for Python2
except ImportError:
    from tkinter import * #for Python3
import sys
sys.path.append("liboro")
from liboro import *

def readData():
    """
    Gets the data from the database and log file.
    Stored as global variables to allow access from all modules.
    """
    global records,logs
    try:
        records = d.getBookRecords()
        logs = bw.getLogRecords()
    except:
        print("READ DATA ERROR")
        
try:
    readData()
except:
    print("ERROR READING DATA")

def bringToFront(window):
    """Brings the given frame to the front when selected"""
    try:
        window.tkraise()
    except:
        print("ERROR RAISING WINDOW")

def createMenu():
    """Main menu window - stores and calls all other frames."""
    #root window definition and attributes
    mainWindow = Tk()
    mainWindow.title("liboro")
    mainWindow.geometry("800x300")
    mainWindow.configure(bg="#E6E6FA")
    #Frame definitions
    mainFrame = Frame(mainWindow,width=800, height=300, bg="white")
    searchFrame = Frame(mainWindow,width=800, height=300,bg="white")
    returnFrame = Frame(mainWindow,width=800, height=300,bg="white")
    checkoutFrame = Frame(mainWindow,width=800, height=300,bg="white")
    weedFrame = Frame(mainWindow,width=800, height=300,bg="white")

    for frame in (mainFrame,searchFrame,returnFrame,checkoutFrame,weedFrame):
        frame.grid(row=0, column=0, sticky='news')

    #main frame attributes
    title = Label(mainFrame, text="liboro", font=("Arial Bold",50),
                  bg='#4B0082', fg='white')
    searchBtn = Button(mainFrame, text="SEARCH",
                       command=lambda:bringToFront(searchFrame))
    returnBtn = Button(mainFrame, text="RETURN",
                       command=lambda:bringToFront(returnFrame))
    checkoutBtn = Button(mainFrame, text="CHECKOUT",
                         command=lambda:bringToFront(checkoutFrame))
    weedBtn = Button(mainFrame, text="WEEDING DATA",
                     command=lambda:bringToFront(weedFrame))

    #main frame layout
    title.place(bordermode=OUTSIDE, height=100,width=800)
    searchBtn.place(bordermode=INSIDE,y=100,height=50,width=800)
    returnBtn.place(bordermode=INSIDE,y=150, height=50,width=800)
    checkoutBtn.place(bordermode=INSIDE,y=200,height=50,width=800)
    weedBtn.place(bordermode=INSIDE,y=250,height=50,width=800)
    
    #frame creation
    try:
        createSearchFrame(searchFrame,mainFrame)
    except:
        print("ERROR CREATING SEARCH FRAME")
    try:
        createReturnFrame(returnFrame,mainFrame)
    except:
        print("ERROR CREATING RETURN FRAME")
    try:
        createCheckoutFrame(checkoutFrame, mainFrame)
    except:
        print("ERROR CREATING CHECKOUT FRAME")
    try:
        createWeedingFrame(weedFrame,mainFrame)
    except:
        print("ERROR CREATING WEEDING FRAME")
    
    
    bringToFront(mainFrame) #starts program on main frame
    mainWindow.mainloop()

def createSearchFrame(searchFrame,mainFrame):
    """Search frame - contains all widgets required to perform a search"""
    #labels
    title = Label(searchFrame, text="BOOK SEARCH", font=("Arial Bold",40),
                  bg='#4B0082', fg='white', anchor=CENTER )
    errorLabel = Label(searchFrame, text="",fg="#FF00FF")
    #entry init
    e = Entry(searchFrame)
    #button init
    idSearchBtn = Button(searchFrame,
                         text="ID SEARCH",
                         command=lambda:bs.showBookById(records,
                                                        e.get(),
                                                        lstBooks,
                                                        errorLabel))
    titleSearchBtn = Button(searchFrame,
                            text="TITLE SEARCH",
                            command=lambda:bs.showBookByTitle(records,
                                                              e.get(),
                                                              lstBooks,
                                                              errorLabel))
    isbnSearchBtn = Button(searchFrame,
                           text="ISBN SEARCH",
                           command=lambda:bs.showBookByISBN(records,
                                                            e.get(),
                                                            lstBooks,
                                                            errorLabel))
    authorSearchBtn = Button(searchFrame,
                             text="AUTHOR SEARCH",
                             command=lambda:bs.showBookByAuthor(records,
                                                                e.get(),
                                                                lstBooks,
                                                                errorLabel))
    mainMenuBtn = Button(searchFrame,
                         text="MAIN MENU",
                         command=lambda:bringToFront(mainFrame))
    #list box init
    lstBooks=Listbox(searchFrame,width=50)
    
    #search frame layouts
    title.place(bordermode=OUTSIDE, height=50,width=800)
    e.place(bordermode=INSIDE,y=50,height=20,width=160)
    idSearchBtn.place(bordermode=INSIDE,y=50,x=160,height=20,width=160)
    titleSearchBtn.place(bordermode=INSIDE,y=50,x=320,height=20,width=160)
    isbnSearchBtn.place(bordermode=INSIDE,y=50,x=480,height=20,width=160)
    authorSearchBtn.place(bordermode=INSIDE,y=50,x=640,height=20,width=160)
    lstBooks.place(bordermode=INSIDE,y=70,height=210,width=800)
    errorLabel.place(bordermode=INSIDE,y=280,height=20,width=400)
    mainMenuBtn.place(bordermode=INSIDE,y=280,x=640,height=20,width=160)

def createReturnFrame(returnFrame,mainFrame):
    """
    Return frame - contains all the widgets required for the user to return a book.
    """
    #labels
    title = Label(returnFrame,
                  text="RETURN BOOKS",
                  font=("Arial Bold",40),
                  bg='#4B0082', fg='white')
    bIdLabel = Label(returnFrame, text="ENTER BOOK ID:")
    mIdLabel = Label(returnFrame, text="ENTER MEMBER ID:")
    errorLabel = Label(returnFrame, text="",fg="#FF00FF")

    #entry init
    bIdEntry = Entry(returnFrame)
    mIdEntry = Entry(returnFrame)

    #button init
    returnBookBtn = Button(returnFrame,
                           text="RETURN BOOK",
                           command=lambda:br.returnBook(records,
                                                        bIdEntry.get(),
                                                        mIdEntry.get(),
                                                        errorLabel))
    mainMenuBtn = Button(returnFrame,
                         text="MAIN MENU",
                         command=lambda:bringToFront(mainFrame))
    confirmBtn = Button(returnFrame,
                        text="COMFIRM CHANGES",
                        command=lambda:d.saveToDatabaseFile(records,errorLabel))

    #return frame layout
    title.place(bordermode=OUTSIDE, height=50,width=800)
    bIdLabel.place(bordermode=INSIDE,y=125,height=20,width=160)
    bIdEntry.place(bordermode=INSIDE,y=125,x=160,height=20,width=160)
    mIdLabel.place(bordermode=INSIDE,y=145,height=20,width=160)
    mIdEntry.place(bordermode=INSIDE,y=145,x=160,height=20,width=160)
    returnBookBtn.place(bordermode=INSIDE,y=165,x=160,height=20,width=160)
    confirmBtn.place(bordermode=INSIDE,y=185,x=160,height=20,width=160)
    errorLabel.place(bordermode=INSIDE,y=260,x=400,height=20,width=400)
    mainMenuBtn.place(bordermode=INSIDE,y=280,x=640,height=20,width=160)

def createCheckoutFrame(checkoutFrame,mainFrame):
    """
    Checkout Frame - contains all the widgets required for the user to checkout a book
    Displays a list of currently available books to chose from.
    """
    #availableBooks = bc.availabilityList(records)
    #label init
    title = Label(checkoutFrame,
                  text="CHECKOUT", font=("Arial Bold",40),
                  bg='#4B0082', fg='white')
    availableBooksLabel = Label(checkoutFrame,
                                text="ALL AVAILABLE BOOKS ARE SHOWN BELOW:")
    bIdLabel = Label(checkoutFrame, text="ENTER BOOK ID:")
    mIdLabel = Label(checkoutFrame, text="ENTER MEMBER ID:")
    errorLabel = Label(checkoutFrame, text="",fg="#FF00FF")
    #entry init
    bIdEntry = Entry(checkoutFrame)
    mIdEntry = Entry(checkoutFrame)
    #button init
    checkoutBookBtn = Button(checkoutFrame, text="CHECKOUT BOOK",
                             command=lambda:bc.checkoutBook(records,
                                                            bIdEntry.get(),
                                                            mIdEntry.get(),
                                                            errorLabel))
    mainMenuBtn = Button(checkoutFrame, text="MAIN MENU",
                         command=lambda:bringToFront(mainFrame))
    confirmBtn = Button(checkoutFrame, text="COMFIRM CHANGES",
                        command=lambda:d.saveToDatabaseFile(records,errorLabel))
    refreshBtn = Button(checkoutFrame, text="REFRESH DATA",
                        command=lambda:showAvailable(lstAvailableBooks))
    
    #list box init
    lstAvailableBooks=Listbox(checkoutFrame,width=70,height=10)
    showAvailable(lstAvailableBooks)
    #displayBookList(lstAvailableBooks,availableBooks)

    #checkout frame layout
    title.place(bordermode=INSIDE, height=50,width=800)
    availableBooksLabel.place(bordermode=INSIDE,y=50,height=20,width=400)
    lstAvailableBooks.place(x=0,y=70)
    bIdLabel.place(bordermode=INSIDE,y=70,x=500,height=20,width=160)
    bIdEntry.place(bordermode=INSIDE,y=90,x=500,height=20,width=160)
    mIdLabel.place(bordermode=INSIDE,y=110,x=500,height=20,width=160)
    mIdEntry.place(bordermode=INSIDE,y=130,x=500,height=20,width=160)
    checkoutBookBtn.place(bordermode=INSIDE,y=150,x=500,height=20,width=160)
    confirmBtn.place(bordermode=INSIDE,y=170,x=500,height=20,width=160)
    refreshBtn.place(bordermode=INSIDE,y=210,x=500,height=20)
    errorLabel.place(bordermode=INSIDE,y=260,x=400,height=20,width=400)
    mainMenuBtn.place(bordermode=INSIDE,y=280,x=640,height=20,width=160)

def showAvailable(lstAvailableBooks):
    try:
        readData()
        availableBooks = bc.availabilityList(records)
        displayBookList(lstAvailableBooks,availableBooks)
    except:
        print("ERROR SHOWING AVAILABLE BOOKS")

def createWeedingFrame(weedFrame,mainFrame):
    """
    Weeding Data Frame - displays a graoh of the book popularity based on checkouts
    """
    title = Label(weedFrame, text="WEEDING DATA", font=("Arial Bold",40),
                  bg='#4B0082', fg='white')
    popLbl = Label(weedFrame, text="",fg='green')
    unpopLbl = Label(weedFrame, text="",fg='red')
    #buttons
    weedingBtn = Button(weedFrame, text="GENERATE WEEDING DATA",
                        command=lambda:showGraph(logs,fig,canvas,lstInfo,
                                                 popLbl,unpopLbl))
    mainMenuBtn = Button(weedFrame, text="MAIN MENU",
                         command=lambda:bringToFront(mainFrame))
    refreshBtn = Button(weedFrame, text="REFRESH DATA",
                        command=lambda:readData())
    #list boxes
    lstInfo=Listbox(weedFrame,width=40,height=5,bg="#FF00FF")
    #graph
    fig=plt.figure(figsize=(5,2))
    canvas = FigureCanvasTkAgg(fig, master=weedFrame)
    
    #weeding layout
    title.place(bordermode=INSIDE, height=50,width=800)
    weedingBtn.place(bordermode=INSIDE,y=50,height=20)
    popLbl.place(bordermode=INSIDE, y=50, x=200, height=20)
    unpopLbl.place(bordermode=INSIDE, y=70, x=200,height=20)
    mainMenuBtn.place(bordermode=INSIDE,y=280,x=640,height=20,width=160)
    lstInfo.place(bordermode=INSIDE, y=110, x=500)
    refreshBtn.place(bordermode=INSIDE,x=500,y=200,height=20)
    canvas.get_tk_widget().place(bordermode=INSIDE,y=90)
    
def displayBookList(lstBox,books):
    """Inserts given list into a given list box"""
    try:
        i=2
        lstBox.delete(0,'end')
        lstBox.insert(1, " ID | ISBN | TITLE | AUTHOR | DATE | HOLDER ID")
        for book in books:
            line='|'.join([str(j) for j in book])
            lstBox.insert(i,line)
            i+=1
    except:
        print("ERROR DISPLAYING BOOK LIST")

def showGraph(logs, fig, canvas,lstInfo,popLbl,unpopLbl):
    """
    Creates a draws book popularity graph to the canvas.
    Log files are used to get the titles and total checkouts of all books.
    """
    bw.formatData(logs,lstInfo,popLbl,unpopLbl)
    try:
        titles = bw.getBookTitles(logs)
        totals = bw.getTotals(logs)
        #sort data by first element in each tuple
        sorted_info = sorted(list(zip(totals,titles)),key=lambda x: x[0])
        totals,titles = list(zip(*sorted_info))
        
        ax1=fig.add_subplot(1,1,1)
        ax1.bar(titles,totals, color="#FF00FF")
        ax1.set_title("Book Popularity")
        ax1.set_xlabel("Books - In the same order as listed on the right.")
        ax1.set_xticks([]) 
        ax1.set_ylabel("Number of checkouts")
        canvas.draw()
    except:
        print("GRAPH ERROR")

try:
    createMenu()#main menu call
except:
    print("MENU ERROR: menu failed to create.")

#Functions are tested with a try,except clause when they are called. 
