# write html
f = open("write-html.py", "w")

#import module
import webbrowser

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

f.write(message)
f.close()

webbrowser.open_new_tab('staytuned.html')
