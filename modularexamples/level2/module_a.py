#just a module with some functions and variables

class A:

    def __init__(self,author = "Yadav Gunjan" ):#constructor with keyword arguments for class defaults
        self.author = author


    def author_name(self):
        print("The author of the module %s is %s"%(self.__class__.__name__,self.author))

from ..level2.module1 import function_call
module1.function_call()