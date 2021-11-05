"""
DATABASE SYSTEM MODULE
Handles reading from and writing to database file.
By F015011
NOV/DEC 2020
"""

def getBookRecords():
    """
    Reads data from database file.
    Each line represents a different copy of a book.
    Information split up by the | character.
    """
    try:
        records=[]
        f=open("database.txt","r")
        for line in f:
            s=line.strip()
            record=s.split("|")
            records.append(record)
        f.close()
        return records
    except:
        print("ERROR READING FROM DATABASE FILE")

def saveToDatabaseFile(records,errorLabel):
    """
    Saves updates made to the book records to the database file
    """
    try:
        f=open("database.txt","w")
        for record in records:
            line = '|'.join([str(i) for i in record])
            f.write("%s\n"%line)
        f.close()
        errorLabel['text']="Changes have been saved successfully."
    except:
        errorLabel['text']="Error - unable to save changes."
        print("ERROR SAVING TO DATABASE FILE")

#Functions are tested with a try,except clause when they are called. 
