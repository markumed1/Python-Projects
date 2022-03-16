# Import tkinter module
import tkinter

# Create GUI window
window = tkinter.Tk()
window.title("Welcome fellow guests")
window.geometry("400x200")

# creating text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()

# create function to set the text with the help of button.
def set_text_by_button():

   # Delete is going to erase anything
    # in the range of 0 and end of file,
    # The respective range given here
    sample_text.delete(0,"end")
    
  
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Enter", 
                    command=set_text_by_button)
  
set_up_button.pack()
  
window.mainloop()
