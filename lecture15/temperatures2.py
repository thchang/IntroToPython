from temp_mod import *

# Ask the user whether to convert F -> C or C -> F
userChoice = input("Please enter F to input a temperature in Fahrenheit,\n" +
                   " or C to input a temperature in Celsius: ")

# If the user enters "F", prompt for tempF and convert to tempC
if userChoice == "F":
    tempF = float(input("Please enter the temperature in degrees Farhenheit: "))
    tempC = F_to_C(tempF)
# Otherwise, prompt for tempC and convert to tempF
else:
    tempC = float(input("Please enter the temperature in degrees Celsius: "))
    tempF = C_to_F(tempC)
# Either way, convert tempC to tempK
tempK = C_to_K(tempC)

# Print all three results using three different techniques
print(f"The freezing point is {FREEZING_POINT_F} degrees F")
print(f"or {FREEZING_POINT_K} Kelvins")
print()
print(f"The temperature in degrees Fahrenheit is: {tempF}")
print()
print("The temperature in degrees Celsius is:", end=" ")
print(tempC)
print()
print("The temperature in Kelvins is: " + str(tempK))
