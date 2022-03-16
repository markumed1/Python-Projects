f = open("write-html.py", "w")

import webbrowser

f = open('staytuned.html', 'w')

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
