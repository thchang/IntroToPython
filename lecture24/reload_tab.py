import csv

# Create an empty list for reloading
reloadedTab = []

# Open myTab.txt file
with open("myTab.csv", "r") as groceryFile:
    # Read in using csv.reader class
    groceryReader = csv.reader(groceryFile)
    for line in groceryReader:
        reloadedTab.append([line[0], float(line[1])])

# Print the reloaded table
for row in reloadedTab:
    print(f"{row[0]}: ${row[1]:.2f}")
