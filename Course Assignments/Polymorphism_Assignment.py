#Parent Class
class Bird:
    wings = "2"
    group = "vertebrates"
    kingdom = "animalia"

    def intro(self):
       print("There are different types of birds")
 
    def flight(self):
       print("Most of the birds can fly but some cannot")


#Child class 2
#polymorphism with inheritance
class parrot(Bird):
    wings = "2"
    group = "vertebrates"
    fly_or_flightless = "fly"
    
    def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
    wings = "2"
    group = "vertebrates"
    fly_or_flightless = "flightless"
    
    def flight(self):
       print("Penguins do not fly")


#Following codes are called for each class
object_bird = Bird()
object_parr = parrot()
object_peng = penguin()
 
object_bird.intro()
object_bird.flight()
 
object_parr.intro()
object_parr.flight()
 
object_peng.intro()
object_peng.flight()











