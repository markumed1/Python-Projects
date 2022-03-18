# Shutil module provides a way for developers to perform various functions
# on a single or grouped files. You can use it to trasnfer files rom a location
# on your computer to another as well as copy and delete files.

# import modules
from tkinter import *
from tkinter.filedialog import askdirectory
import shutil
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import filedialog

# Path
path = '/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment/HomeA/'
 
# Get the time of last
# modification of the specified
# path since the epoch
modification_time = os.path.getmtime(path)

 
# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)


if Path('/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment/HomeA/').is_file():
    print ("File exist")
else:
    print ("File not exist")
    
#set where the source of the files are
source = '/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment/HomeA/'

#set the destiation path to folderB
destination = '/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment/HomeB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
    


# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
      
      
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)




#date within 24 hours
if now-timedelta(hours=24) <= set_date <= now+timedelta(hours=24):
     raise ValidationError('')

if __name__ == "__main__":
    window.mainloop()  
