#Create class
class dog:
    #Assign values to object properties using the __init__()function.
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def myfunc(self):
        print("The breed of my dog is a " + self.breed)


#Create Object
animal = dog("Pug", "apricot")
animal.myfunc()






