# Import modules.
import os
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )


# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)

open_button.pack(expand=True)

root.mainloop()


# The Path
path = '/Users/Marku/OneDrive/Desktop/'


# Get the time of last modification of the specified path
try:
    modification_time = os.path.getmtime(path)
    print("Last modification time since the epoch:", modification_time)
 
except OSError:
    print("Path '%s' does not exists or is inaccessible" %path)
    sys.exit()
 
# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)






    












    
