# Declare named constants
CAD_TO_USD = 0.78
EUR_TO_USD = 1.09
GBP_TO_USD = 1.30

# Get input from the user: CAD/EUR/GBP to convert
convertType = input("What type of currency would you like to convert to USD? (CAD/EUR/GBP: ")

# Case #1 -- user enters CAD -> USD
if convertType == "CAD":
    cad = float(input("Please enter the amount of CAD to convert: "))
    usd = cad * CAD_TO_USD

# Case #2 -- user enters EUR -> USD
elif convertType == "EUR":
    eur = float(input("Please enter the amount of EUR to convert: "))
    usd = eur * EUR_TO_USD

# Case #3 -- user enters GBP -> USD
elif convertType == "GBP":
    gbp = float(input("Please enter the amount of GBP to convert: "))
    usd = gbp * GBP_TO_USD

# Case #5 -- bad input
else:
    print("Error: Input was not on the list (CAD/EUR/GBP)")
    usd = -1.0

# If usd is negative, don't print anything
if usd > 0:
    print(f"The amount in USD is: {usd:.2f}")
