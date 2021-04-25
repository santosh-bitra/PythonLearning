# Fizz at every number divisible by 3
# Buzz at evey number divisible by 5
# FizzBuzz at evey number divisible by both 3 and 5

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

