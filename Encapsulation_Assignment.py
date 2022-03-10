# Protected is prefixed with a SINGLE underscore. Doesn't change the behaviour of anything.
# Methods and properties can still be modified.
# Protected variable: 
class Protected:
    def __init__(self):
        self._protectedVar = 10

obj = Protected()
obj._protectedVar = 100
print(obj._protectedVar)


# Private is denoted with a DOUBLE underscore prefix.
class Protected:
    def __init__(self):
        self.__privateVar = 35

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


# Obj gets the data of the private variable, also set privateVar a new rule. Ask
# for it to be retrieved. Ensures that private can not be changed unless it is on purpose.
obj = Protected()
obj.getPrivate()
obj.setPrivate(75)
obj.getPrivate()
