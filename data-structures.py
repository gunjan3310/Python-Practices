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

#list comprehensions examples
cordinates = [(x,y) for x in range(6) for y in range(0,6) if x==y]
print("Cordinates for line y=x",cordinates)

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
transposed = [[row[i] for row in matrix] for i in range(4)] #nested list comprehension it's difficult withour famailirity
print(transposed)

#sets
print("Sets and their usage")
a = set('abcdefghijklmnopqrstuvwxyz')
b = set('Gunjan Yadav')

print("letters in a or b or both",a|b)
print("letters in a but not in b",a-b)
print("letters in both a and b",(a&b))
print("letter in a or b but not in both",a^b)
#list comprehension in set

setcomprehension = {x for x in range(6)}
print("Set comprehended ", setcomprehension)