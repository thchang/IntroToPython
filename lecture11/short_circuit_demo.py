# Get a numerical input from the user
userInput = float(input("Enter a number: "))

# Check whether 1 / userInput < 4
if (userInput != 0) and (1 / userInput < 4): # Check will short-circuit
    print("That number was > 1/4")
else:
    print("That number was <= 1/4")
