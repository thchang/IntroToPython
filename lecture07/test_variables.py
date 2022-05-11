x = 1 # Create a variable named x
x = 2 # Set x = 2
x + 1 # Does nothing
print(x) # x should be 2 here
x = x + 1 # Add +1 to x
print(x) # x should be 3 here
y = x # New variable y = 3
x = x + 1 # Updates x, but not y
print(x)
print(y)
