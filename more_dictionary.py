#constructor method for dictonary
dict_smooth = dict(a = 0, b = 1, c = 2)
print(dict_smooth)

dict_smooth2 = dict([("a2",0),("b2",1),("c2",2)])
print(dict_smooth2)

keys = ['a3','b3','c3']
values = [0,1,2]
dict_smooth3 = dict(zip(keys,values))
print(dict_smooth3)

#awesome 'list comprehension' method
keys = ('d','e','f')
awesome_dict = {keys[x-3] + '4':x for x in range(3,6)}
print(awesome_dict)

#gutting dictionaries keys and values
print('---------------------')

for k in awesome_dict.keys():
    print(k)
print('Values are:')
for v in awesome_dict.values():
    print(v)

print('----------------------')

#merging dictionaries
final_dict = dict(dict_smooth, **dict_smooth2, **dict_smooth3,**awesome_dict)
print(final_dict)