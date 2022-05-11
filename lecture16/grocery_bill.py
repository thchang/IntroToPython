# Define the grocery list
groceryList = ("apples", "bananas", "lettuce", "chicken", "beans")
priceList = [0.0] * len(groceryList)

# Print some welcome messages
print("Welcome to the grocery bill calculator!")
print("Please enter the price of 5 items that you will purchase.")

# Calculate the running total with a for-loop
total = 0.0
for i in range(len(groceryList)):
    priceList[i] = float(input(f"Please enter the price of {groceryList[i]}: "))
    total += priceList[i]

# Print the results
for i in range(len(groceryList)):
    print(f"{groceryList[i]}:\t${priceList[i]:.2f}")
print("--------------------------------")
print(f"Total:\t${total:.2f}")
