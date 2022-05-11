# Create named constant
CAD_TO_USD = 0.78

# Try to read input from user
try:
    cad = float(input("Please enter the amount of CAD to convert: "))
# If a non-numeric input was given, assign cad = -1.0
except ValueError:
    cad = -1.0

# Use an input validation loop to force a non-negative number
while cad < 0:
    try:
        cad = float(input("Illegal input. Please try again: "))
    except ValueError:
        cad = -1.0 # Always replace non-numeric values with -1.0

# Perform the conversion
usd = cad * CAD_TO_USD

# Print the result
print(f"The amount in USD is: {usd:.2f}")
