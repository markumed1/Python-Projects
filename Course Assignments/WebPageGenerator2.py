

def webPage(name, bio):
  #web = name+".html"
  web = "biopage.html"
  openFile = open(web, "w+")
  
  openFile.write("<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>"+name+"</h1>\n\t</center>\n\t<hr />\n\t"+bio+"\n\t<hr />\n</body>\n</html>")

  openFile.close()



webbrowser.open_new_tab('biopage.html')

