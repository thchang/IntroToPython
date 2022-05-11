# Define the grocery list and initialize price list
groceryTab = []

# Print some welcome messages
print("Welcome to the grocery bill calculator!")
print("Please enter the price of 5 items that you will purchase.")

# Get names and prices from user and store in dynamically expanding lists
nextName = input("Please enter the name of an item to purchase. (Type 'q' to quit): ")
while nextName != "q":
    nextPrice = float(input(f"Please enter the price of {nextName}: "))
    groceryTab.append([nextName, nextPrice])
    nextName = input("Please enter the name of an item to purchase. (Type 'q' to quit): ")

# Print the results
total = 0.0
for row in groceryTab:
    print(f"{row[0]}:\t${row[1]:.2f}")
    total += row[1]
print("--------------------------------")
print(f"Total:\t${total:.2f}")
