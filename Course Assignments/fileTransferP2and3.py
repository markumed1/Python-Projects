# Import modules.
import os
import time
import sys
import shutil
import datetime
from datetime import date
from datetime import timedelta
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


	

# Defining CreateWidgets() function to
# create necessary tkinter widgets
def CreateWidgets():
	link_Label = Label(root, text ="Select The File To Copy : ",
					bg = "#E8D579")
	link_Label.grid(row = 1, column = 0,
					pady = 5, padx = 5)
	
	root.sourceText = Entry(root, width = 50,
							textvariable = sourceLocation)
	root.sourceText.grid(row = 1, column = 1,
						pady = 5, padx = 5,
						columnspan = 2)
	
	source_browseButton = Button(root, text ="Browse",
								command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 1, column = 3,
							pady = 5, padx = 5)
	
	destinationLabel = Label(root, text ="Select The Destination : ",
							bg ="#E8D579")
	destinationLabel.grid(row = 2, column = 0,
						pady = 5, padx = 5)
	
	root.destinationText = Entry(root, width = 50,
								textvariable = destinationLocation)
	root.destinationText.grid(row = 2, column = 1,
							pady = 5, padx = 5,
							columnspan = 2)
	
	dest_browseButton = Button(root, text ="Browse",
							command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 2, column = 3,
						pady = 5, padx = 5)
	
	copyButton = Button(root, text ="Copy File",
						command = CopyFile, width = 15)
	copyButton.grid(row = 3, column = 1,
					pady = 5, padx = 5)
	

def SourceBrowse():
	# Opening the file-dialog directory prompting
	# the user to select files to copy using
	# filedialog.askopenfilenames() method. Setting
	# initialdir argument is optional Since multiple
	# files may be selected, converting the selection
	# to list using list()
	sourcedirectory = filedialog.askdirectory()
	
	# Displaying the selected file path in the entry widget.
	root.sourceText.insert('1', sourcedirectory)
	
def DestinationBrowse():
	# Opening the file-dialog directory prompting
	# the user to select destination folder to
	# which files are to be copied using the
	# filedialog.askopendirectory() method.
	# Setting initialdir argument is optional
	destinationdirectory = filedialog.askdirectory()

	# Displaying the selected directory in the
	# root.destinationText Entry using
	# root.destinationText.insert()
	root.destinationText.insert('1', destinationdirectory)
	
def CopyFile():
	# Retrieving the source file selected by the
	# user in the SourceBrowse() and storing it in a
	# variable named files_list
	files = os.listdir(root.sourceText.get())

	# Retrieving the destination location from the
	# textvariable using destinationLocation.get() and
	# storing in destination_location
	destination_location = destinationLocation.get()

	# Looping through the files present in the list
	for f in files:
		
		# Copying the file to the destination using
		# the copy() of shutil module copy take the
		# source file and the destination folder as
		# the arguments
		print(f, destination_location)
		print(root.sourceText.get())
		sourceFile = root.sourceText.get() + "/" + f
		print(sourceFile)
##              assign current date/time to a variable as Today
		current_time = datetime.datetime.now()
		print("Current date and time is : ", end = "")
		print(current_time)
		
##		assign Yesterday = today - 24 hours
		today = date.today()
		yesterday = today - timedelta(days = 1)
		print(today)
		print(yesterday)

		
##		get the modification date of the sourceFile (not path)
		modification_time = os.path.getmtime(sourceFile)
		print("Last modification time since the epoch:", modification_time)
		
##		if the modification date of sourceFile is greater than Yesterday
##		then move the file else do nothing
		local_time = time.ctime(modification_time)
		print("Last modification time(Local time):", local_time)

		shutil.copy(sourceFile, destination_location)
                
	messagebox.showinfo("SUCCESSFUL")


	






# Creating object of tk class
root = tk.Tk()
	
# Setting the title and background color
# disabling the resizing property
root.geometry("830x120")
root.title("Copy-Move GUI")
root.config(background = "black")
	
# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()
	
# Calling the CreateWidgets() function
CreateWidgets()
	
# Defining infinite loop
root.mainloop()










if __name__ == "__main__":
    window.mainloop()

    












    
