Structure of files:
The main program is run from the "menu.py" file which imports the package "liboro" containing all other modules; the database and log files are in the same directory as the menu file.
Database and log text files:
The log file is written in the same format as the text file in order to allow reuse of functions such as searching for a given book title.
Searching:
The book searching has options for searching by id, title, ISBN, and Author; the title and author searches are case sensitive. 
Book weeding:
The book weeding data is based on book popularity which is calculated by the number of checkouts seen within the log file of a given book. Therefore, the program displays the most and least popular books to the user in order for them to make their own decision about which books to remove from the library. This data is presented as a bar chart with a list of the data shown next to it as a key because the titles would otherwise be too long to display.
Testing:
Each function is tested when it is called using a try, except clause; if there is an error with a functions use, this will be indicated within the console with an error message.