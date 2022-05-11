# Define the grocery list
groceryList = ["apples", "bananas", "lettuce", "chicken", "beans"]

# Print some welcome messages
print("Welcome to the grocery bill calculator!")
print("Please enter the price of 5 items that you will purchase.")

# Calculate the running total with a for-loop
total = 0.0
for item in groceryList:
    price = float(input(f"Please enter the price of {item}: "))
    total += price

# Print the results
print(f"Your total bill is ${total:.2f}")
