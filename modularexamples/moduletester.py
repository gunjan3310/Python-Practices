from modularexamples.module1 import fib,fib2 #fib and fib2 are registered in the local symbol table

fib(10)
print(fib2(20))

def fib(n): #local symbol table gets redefined for fib()
    print('fib of current module %d' %n)
fib(10)
from modularexamples.module1 import * #the symbol table is updated again
fib(20)