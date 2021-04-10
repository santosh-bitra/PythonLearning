'''Program to check if your name is in the list or not
The used objects in the below python program covers list, input() function, if-else, in-membership operator, and "+" operator and print() function.'''

#Start of the actual program below:

names  = ["Santosh", "Aarya", "Hari", "Chulbul", "Mouli"]
x = input("What is  your name?");
if (x in names):
    print("Hello,", x )
else:
    print("Am sorry, " + x + " your name is not in our list")
