# Python program to explain os.path.getmtime() method

# importing os and time module
import os
import time

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
