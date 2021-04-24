# Replacing the Values in Treasure Hunt

'''This program covers the following: 
1. List creation
2. Nested list creation
3. Usage of positions
4. Input splitting
5. Values replacing in the list
'''

# We first define contents or charecters in each rows. These are 'lists'
row_1 = ["😞", "❤", "🔥"]
row_2 = ["🐻", "🍨", "🛹"]
row_3 = ["💣", "🦁", "💋"]

# Now we create a Nested List
map = [row_1, row_2, row_3]

# Now we see the output to understand how it looks like
print(f" {map[0]}\n {map[1]}\n {map[2]}\n")

# Taking the user input for the position seperated by commas
position = input("Enter your position ").split(",")

# Converting the values to input to integers
x = int(position[0])  #2
y = int(position[1])  #3

# Mapping the value we want to see at the positions we want it to be seen at
map[x - 1][y - 1] = "WIN"

# Printing the new amended output
print(f" {map[0]}\n {map[1]}\n {map[2]}\n")

