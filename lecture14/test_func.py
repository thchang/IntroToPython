x = 3 # A global variable x

def my_func(): # Define a function my_func
    x = 2 # Update local copy of x
    print(x)
    return

my_func() # Call my_func
print(x) # Prints the global copy
