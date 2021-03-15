#
#
# Python:   3.9
#
# Author:   John Trump
#           
#
# Purpose:  Create DataBase using Python and the sqlite3 module which has 2 fields:
#           an auto-increment primary integer field and a data type "string field".
#               1) The code will need to iterate through a supplied list of file
#                   names to determine which ends with ".txt"
#               2) The code will then add those ".txt" files to the database.
#               3) Lastly the desired information will be printed to the console.



import sqlite3              #bring in the sqlite3 module for use

conn = sqlite3.connect('Assignment.db')  #creates the database

with conn:                  #creates the table with the two columns
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_txtFile TEXT)") 
    conn.commit()
conn.close()


import sqlite3              #bring in the sqlite3 module for use

conn = sqlite3.connect('Assignment.db')

# the creation of the tuple to be parsed through:

fileList_Tuple = ('information.docx', 'Hello.txt', 'myimage.png', \
            'myMovie.png', ' World.txt', 'data.pdf', 'myPhoto.jpg')


# the loop to parse out the ".txt" files and add to the table

for x in fileList_Tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_txtFile) VALUES (?)", (x,))
            print(x)
conn.close()

