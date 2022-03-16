# write html
f = open("write-html.py", "w")

#import module
import webbrowser
import tkinter

# Create GUI window
window = tkinter.Tk()
window.title("Welcome fellow guests")
window.geometry("400x200")

# "w" Write - will overwrite any existing content
f = open('staytuned.html', 'w')

# enter message with """ """
message = """<html>
  <body>
   <h1>
      Stay tuned for our amazing summer sale!
    </h1>
  </body>
</html>"""


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


if __name__ == "__main__":
    set_up_button.pack()
    window.mainloop()
    f.write(message)
    f.close()

webbrowser.open_new_tab('staytuned.html')
