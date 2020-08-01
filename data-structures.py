# these are some of the premitive data structures in python

#numbers
from builtins import print

integer = 1
decimal = 1.0

#strings

firstname = "Gunjan"
lastname = 'Yadav'

#list of items in python

list_of_name_attributes = ["firstname","lastname"]
list_of_integer = [1,34,5,76,2]

#tuples are unlike list with the feature that they dont update later after defination

basic_people_info = ("name","address","phone")

#dictionary data structure in python is essentially a key/value pair data organization

myDict = {
    "key_one" : "fruit",
    "data_structure" : "dictionary",
    "1995":"olymics"
}

#little bit on relevent topic of data structure is assignments on variables

a = b = c = 1

#Now Let's print all that we have initillized

print(integer)
print(firstname)
print(lastname)
print("Printing a list: ",list_of_name_attributes)
print("Printing list of integers", list_of_integer)
print("A touple: ",basic_people_info)
print("The key value dictionary in total", myDict)

#Dictionary specific features
print("myDict has 'data_structure' key and the associated value upon call is: ",myDict["data_structure"])