# Create an empty list for reloading
reloadedTab = []

# Open myTab.txt file
with open("myTab.txt", "r") as groceryFile:
    for line in groceryFile:
        line.strip() # Strip whitespace off the front/end of line
        cols = line.split() # Split into a list
        reloadedTab.append([cols[0], float(cols[1])])

# Print the reloaded table
for row in reloadedTab:
    print(f"{row[0]}: ${row[1]:.2f}")
