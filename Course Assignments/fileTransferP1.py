# Shutil module provides a way for developers to perform various functions
# on a single or grouped files. You can use it to trasnfer files rom a location
# on your computer to another as well as copy and delete files.

import shutil
import os

#set where the source of the files are
source = '/Users/Marku/OneDrive/Desktop/FolderA/'

#set the destiation path to folderB
destination = '/Users/Marku/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
    
