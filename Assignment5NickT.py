def FToC(fahrenheit):
    celsius = (fahrenheit - 32) * (5.0/9.0)
    return celsius
    
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    



