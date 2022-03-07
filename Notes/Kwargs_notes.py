#Kwargs is short for "keyword arguments". and is also a special syntax.
#its written as **kwargs. The asterisks ** represent a key value pair.
def myFun(**kwargs):
    print("kwargs", kwargs)

myFun(first = "1", second = "2", third = "3")
