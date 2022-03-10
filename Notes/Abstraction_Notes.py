# creating abstract methods.
# "abstractmethod" from the abc module (Abstract Base Class).
from abc import ABC, abstractmethod
class gym(ABC):
    def memberFee(self, amount):
        print("Your monthly dues are: ",amount)
# This function is telling us to pass in argument
    @abstractmethod
    def payment(self, amount):
        pass

class DebitorCreditCardPayment(gym):
    # implemented the payment function from its parent memberFee class.
        def payment(self, amount):
            print('Thank you for paying the dues of of {} on time.  '.format(amount))

obj = DebitorCreditCardPayment()
obj.memberFee("$150")
obj.payment("$150")


    
