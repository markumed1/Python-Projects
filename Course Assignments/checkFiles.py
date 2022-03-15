# Importing tkinter module
from tkinter import *

# Createing a tkinter window
root = Tk()

# Initializing tkinter window
# with dimensions 300 x 250
root.geometry('500x160')

# add title to window
root.title('Check List')

# creating a buttons for browse, check files and close program
btn1 = Button(root, text = 'Browse...', width = 12)
btn1.place(x=15, y=40)

btn2 = Button(root, text = 'Browse...', width = 12)
btn2.place(x=15, y=80)

btn3 = Button(root, text = 'Check for files...', width = 12, height = 2)
btn3.place(x=15, y=112)

btn4 = Button(root, text = 'Close Program', width = 12, height = 2)
btn4.place(x=385, y=113)


# Creating entry widgets
txtfld=Entry(root, width = 56, bd=1)
txtfld.place(x=140, y=40)

txtfld=Entry(root, width = 56, bd=1)
txtfld.place(x=140, y=80)

