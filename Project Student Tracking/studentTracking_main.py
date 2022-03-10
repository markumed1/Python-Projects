# Python Ver: 3.10.2
#
# Author: Mark Medrano
#
# Purpose: Student Tracking System Application Demo
#          using Python with Tkinter and SQLite3.
#
# Tested OS: This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import studentTracking_gui
import studentTracking_func


# Frame is the Tkinter fram class that out own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(600,400) # (Height, Width)
        self.master.maxsize(600,400)
        #This CenterWindow method will center our app on the user's screen
        studentTracking_func.center_window(self,600,400)
        self.master.title("Student Tracking Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter buil-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentTracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seprate module,
        # keeping your code comparmentalized and clutter free
        studentTracking_gui.load_gui(self)





if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
