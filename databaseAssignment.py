# The import keyword is used to import modules.
import sqlite3


# Establish connection with the database
conn = sqlite3.connect('test.db')


"""While connection is open you get the cursor off connection
and use the cursor to send SQL command in database.
Create Table"""
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_docx TEXT, \
        col_txt TEXT, \
        col_pdf TEXT, \
        col_png TEXT, \
        col_mpg TEXT, \
        col_jpg TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

# tuple of files
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# loop through each object in the tuple to find files ending with .txt.
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # value for each row will be one name of out the tuple (x,)
        # will denote a one element tuple for each name ending with .txt
            cur.execute("INSERT INTO tbl_files (col_txt) VALUES (?)", (x,))
            print(x)

conn.close()
