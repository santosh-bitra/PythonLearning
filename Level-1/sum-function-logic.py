#The program explaining the logic behind 'sum.function'

'''This below program takes the list of values and add them all one by one 
using a for loop and the given logic to give the sum of all values in the List'''

# Pre-Defined List Below 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A for loop to convert every value in the List from string to integer
for n in range(0, len(List)):
    List[n] = int(List[n])
print(List)

# Pre-Defining Value of a variable x which I am going to use in the addition logic
x = 0

# The below is the logic for sum fucntion.
for i in List:
    x += i

# Prints the final sum of all values in the List
print(x)

