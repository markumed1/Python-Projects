#"Args" is short for "arguments"
def myFun(*args):
    for arg in args:
        print (arg)

myFun('This is an example of args', 'string', 'and then and integer', 5)
