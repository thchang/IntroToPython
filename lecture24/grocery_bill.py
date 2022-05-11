import csv

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

# Write the results to a CSV file using csv.writer class
with open("myTab.csv", "a") as groceryFile:
    groceryWriter = csv.writer(groceryFile)
    for row in groceryTab:
        groceryWriter.writerow(row)
