# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__": #when this module is executed this main will be called
    import sys #imported from standard python packages
    print("Ok the module is run")
    for n in sys.argv[1:]:
        fib(int(n))
def function_call():
    print("Printing a function from module1")
