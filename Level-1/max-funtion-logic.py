# Average Height Calculator

'''This below program takes the list of values and compares them all one by one
using a for loop and the given logic to give the highest value of the List'''


# Defining the values in random divided by a ','
List = input("Provide list of students height").split(",")

# A for loop to convert every value in the List from string to integer
for n in range(0, len(List)):
    List[n] = int(List[n])
print(List)

# Pre-Defining Value of a variable x which I am going to use in the comparision logic
x = 0

# The below is the logic for max fucntion.
for i in List:
    if i > x:
        x = i

# Prints the final sum of all values in the List
print(x)

