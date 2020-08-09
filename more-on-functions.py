#function behaviour on default value arguments
i =1
def fun(args = i):
    print(args)
    return args
i=2
print("Function call prints %d"% fun())

#symbol table maintains default arguments state -- very important, without this a problem might lead to madness
print("symbol table maintains default arguments state")
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#keyword arguments helps to maintain ease of passing arguments in ambiguity of usecase
print("\nKeyword Arguments\n")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.(_first arg)",
           "It's really very, VERY runny, sir.(var length arg list)",
           shopkeeper="Michael Palin",#from here on its named args, while function is being used. args_list could be handy
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print("\nSpecial parameters aren't taken into account here\n")