# Encapsulate means to enclose. Encapsulation is an important
# aspect to Object-Oriented programming. The purpose is to wrap
# your code in one single unit that restricts access from functions
# and variables from being directly changed or modified by accident
# within a class.
class Protected:
    def __init__(self):
        self.protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

# Encapsulation is implemented by creating a protected (also called non-public)
# or private method or property.








# Private is denoted with a double underscore prefix. It’s harder to access
# but can still be done.
class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self.__privateVar  = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

# Above, Obj gets the data of the private variable, but then we also set the privateVar a new value.
# We then ask for that to be retrieved. It takes a bit more coding, but this ensures that private can
# not be changed unless it is on purpose. The output for this code is: 12, 23
