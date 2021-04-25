# Program to add all even numbers between 1 and 100

# Method 1
x = 0
for i in range(0, 100, 2):
    x = x + i
print(x)

# Method 2
y = 0
for number in range(0, 100):
    if number % 2 == 0:
        y = number + y
print(y)
