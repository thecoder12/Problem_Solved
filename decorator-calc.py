
def printme(function):
    def wrapper(*args, **kwargs):
        print(function.__name__, *args, end = ' = ')
        return function(*args, **kwargs)
    return(wrapper)

@printme
def add(a,b):
    return(a+b)

@printme
def sub(a,b):
    return(a-b)

@printme
def mul(a,b):
    return(a*b)

print(add(3,4))
print(sub(5,2))
print(mul(2,3))
