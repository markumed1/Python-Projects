from tkinter import filedialog
import os
								# Where it open to.					# What the window is called.
folder = filedialog.askdirectory(initialdir=os.path.normpath("C:/Users/Marku/OneDrive/Desktop/Main File"), title="Directory")
