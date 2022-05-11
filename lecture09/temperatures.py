# Named constants
FREEZING_POINT_F = 32
FREEZING_POINT_K = 273.15

# Get input in degrees F
tempF = float(input("Please enter the temperature in degrees Farhenheit: "))

# Perform calculations to convert to deg C and Kelvins
tempC = (tempF - FREEZING_POINT_F) * 5 / 9
tempK = tempC + FREEZING_POINT_K

# Print output using 2 different techniques
print()
print("The temperature in degrees Celsius is:", end=" ")
print(tempC)
print()
print("The temperature in Kelvins is: " + str(tempK))
