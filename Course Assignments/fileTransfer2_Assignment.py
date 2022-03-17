# import modules to organize files of a directory
import shutil
from datetime import date
import os
import sys

# When there is need, just change the directory
os.chdir(sys.path[0])

# Function for performing the
# backup of the files and folders
def take_backup(src_file_name, 
                dst_file_name=None,
                src_dir='', 
                dst_dir=''):
    try:

         # Extract the today's date
        today = date.today()  
        date_format = today.strftime("%d_%b_%Y_")

        # Make the source directory,
        # where we wanna backup our files
        src_dir = 'C:\Users\Marku\OneDrive\Desktop\GitHub\Python-Projects\Course Assignments\File Transfer Assignment\HomeFiles'
    


