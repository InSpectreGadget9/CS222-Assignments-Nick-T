def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0
        
    