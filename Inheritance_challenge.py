#Parent
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


#Child/Inheritance 
class Student(Person):
  pass

x = Student("Mos", "Def")
x.printname()
