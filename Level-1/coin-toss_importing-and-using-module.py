'''Consider this to be a small basic example of how to call and use modules in a script.
The below has a commented leapyear script and a working heads or tails programme which declares either
by determining whether a random number called is an odd or an even number.
Happy Learning'''

#from datetime import month
#today = month.today()
#print(today)
#x = int(input("Your Year : "))
#print(bool(x % 4 == 0 or (x % 100 == 0 and x % 400 == 0)))

#Import Random module
import random

#declaring variable, using randint from random module to call a random int from a list of numbers between 1 to 100.
input = random.randint(1,100)


if int(input) % 2 == 0:
      print("Heads")
else:
      print("Tails")




'''
x = range(1, 20)
y = random.choice(x)

if y % 2 == 0:
      print(f"{y} in an even number")
else:
      print(y, "is not an even number")
'''
