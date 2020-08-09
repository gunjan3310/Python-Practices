#checking wether a number is odd or even
import sys

def if_else(number):

    #number = int(input("Enter a number here: "))

    if (number)%2 == 0:
        print("The number % d is even" %(number))
    else:
        print("The number % d is odd" %(number))

    if number == 0:
        print("This on the origin")
    elif number < 0:
        print("Number is towards the negative half")
    elif number >0 :
        print("Number %d is on the positive half"%(number))

def for_loop(list1 = list(("abc","def","ghi"))): #default argument for function when nothing is provided as list
    print("For loop in work")
    for item in list1:
        print(item)
list1 = list((1,2,3,4,5,6))
for_loop(list1)
for_loop() #default argument itteration from function decleration
for num in list1:
    if_else(num)

