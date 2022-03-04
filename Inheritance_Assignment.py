#Create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Mos", "Def")
x.printname()

#Child classes that inherit their parent class

class Student(Person):
    pass

x = Student("Mike", "Thompson")
x.printname()


class Teacher(Person):
    pass

x = Teacher("Tom", "Nalen")
x.printname()
