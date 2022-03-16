import webbrowser
import tkinter


# enter message with """ """
message = """<html>
  <body>
   <h1>
      Stay tuned for our amazing summer sale!
    </h1>
  </body>
</html>"""


# create function to set the text with the help of button.
def set_text_by_button():

    # "w" Write - will overwrite any existing content
    f = open('staytuned.html', 'w')
    message = sample_text.get()
    print (message)
   
    f.write(message)
    f.close()
    webbrowser.open_new_tab('staytuned.html')
    
    # Delete is going to erase anything
    # The respective range given here 
    # in the range of 0 and end of file,
    sample_text.delete(0,"end")
    
# Set up the GUI
# Create GUI window
window = tkinter.Tk()
window.title("Welcome fellow guests")
window.geometry("400x200")

# creating text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()
# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Enter", 
                    command=set_text_by_button)
set_up_button.pack()

if __name__ == "__main__":
    window.mainloop()



