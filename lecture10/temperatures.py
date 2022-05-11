# Named constants
FREEZING_POINT_F = 32
FREEZING_POINT_K = 273.15

# Ask the user whether to convert F -> C or C -> F
userChoice = input("Please enter F to input a temperature in Fahrenheit,\n" +
                   " or C to input a temperature in Celsius: ")

# If the user enters "F", prompt for tempF and convert to tempC
if userChoice == "F":
    tempF = float(input("Please enter the temperature in degrees Farhenheit: "))
    tempC = (tempF - FREEZING_POINT_F) * 5 / 9
# Otherwise, prompt for tempC and convert to tempF
else:
    tempC = float(input("Please enter the temperature in degrees Celsius: "))
    tempF = (tempC * 9 / 5) + FREEZING_POINT_F
# Either way, convert tempC to tempK
tempK = tempC + FREEZING_POINT_K

# Print all three results using three different techniques
print()
print(f"The temperature in degrees Fahrenheit is: {tempF}")
print()
print("The temperature in degrees Celsius is:", end=" ")
print(tempC)
print()
print("The temperature in Kelvins is: " + str(tempK))
