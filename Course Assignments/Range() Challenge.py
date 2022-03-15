Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x range(0, 1, 2, 3)
SyntaxError: invalid syntax
x = range(0, 1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x = range(0, 1, 2, 3)
TypeError: range expected at most 3 arguments, got 4

= RESTART: C:/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/Range() Challenge.py
Traceback (most recent call last):
  File "C:/Users/Marku/OneDrive/Desktop/GitHub/Python-Projects/Course Assignments/Range() Challenge.py", line 1, in <module>
    x = range(0, 1, 2, 3)
TypeError: range expected at most 3 arguments, got 4
x = range(4)
for n in x:
    print(n)

    
0
1
2
3
x range(3, 0, 1)
SyntaxError: invalid syntax
x = range(3, 0, 1)
print n in x:
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
for n in x:
    print(n)

    


================================ RESTART: Shell ================================
x range = (3, 1, 1)
SyntaxError: invalid syntax
x = range(3, 1, 1)
for n in x:
    print(n)

    
x range(3, -1, -1)
SyntaxError: invalid syntax

================================ RESTART: Shell ================================
x = range(3, -1, -1)
for n in x:
    print(n)

    
3
2
1
0



x = range(8, -2, 1)
for n in x:
    print(n)

    

x = range(8, -2, -1)
for n in x:
    print(n)

    
8
7
6
5
4
3
2
1
0
-1
x range(8, -2, 3)
SyntaxError: invalid syntax
x = range(8, -2, 3)
for n in x:
    print(n)

    

x = range(8, -2, 0)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x = range(8, -2, 0)
ValueError: range() arg 3 must not be zero
x = range(8, -2, 2)
for n in x:
    print(n)

    






x = range(8, -2)
for n in x:
    print(n)

    

x = range(8, 1, -2)
for n in x:
    print(n)

    
8
6
4
2
