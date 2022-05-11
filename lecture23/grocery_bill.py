# Define grocery list and initialize price list
groceryTab = []

# Print some welcome messages
print("Welcome to the grocery bill calculator!")
print("Please enter the name and price of all items that you will purchase.")

# Get names and prices from user and store in dynamically expanding lists
nextName = input("Please enter the name of an item to purchase. (Type 'q' to quit): ")
while nextName.lower() != "q":
    nextPrice = float(input(f"Please enter the price of {nextName}: "))
    groceryTab.append([nextName, nextPrice])
    nextName = input("Please enter the name of an item to purchase. (Type 'q' to quit): ")

## Print the results
#total = 0.0
#for row in groceryTab:
#    print(f"{row[0]}:\t${row[1]:.2f}")
#    total += row[1]
#print("-------------------------------")
#print(f"Total:\t${total:.2f}")

# Write the results to a file
with open("myTab.txt", "a") as groceryFile:
    for row in groceryTab:
        groceryFile.write(f"{row[0]} {row[1]}\n")
