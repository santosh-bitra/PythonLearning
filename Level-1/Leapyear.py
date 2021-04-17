#Program to calculate if a given year is a leap year on not

x = int(input("Please enter the year to be checked"))

if bool(x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)) == True:
    print("Leap Year")
else:
    print("Not a leap year")

