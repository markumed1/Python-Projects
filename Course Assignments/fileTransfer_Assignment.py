# Shutil module provides a way for developers to perform various functions
# on a single or grouped files. You can use it to trasnfer files rom a location
# on your computer to another as well as copy and delete files.

# import modules
from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil
import os
import time
from datetime import datetime, timedelta
from pathlib import Path


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
    

 
# shows dialog box and return the path
path = askdirectory(title='/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/File Transfer Assignment/HomeA/') 
print(path)


#date within 24 hours
if now-timedelta(hours=24) <= set_date <= now+timedelta(hours=24):
     raise ValidationError('')
     
