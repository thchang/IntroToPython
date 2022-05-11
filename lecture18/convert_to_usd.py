CAD_TO_USD = 0.78
EUR_TO_USD = 1.09
GBP_TO_USD = 1.30

go = True # Flag variable

# Main execution loop
while go:

    # Get input from the user: CAD/EUR/GBP to convert, q to quit
    convertType = input("What type of currency would you like to convert to USD?\n" +
                        "Enter one of the following: 'CAD', 'EUR', or 'GBP'.\n" +
                        "Or enter 'q' to quit\n>>> ")
    
    # Case #1 -- user enters CAD -> USD
    if convertType == "CAD":
        # Use an input validation loop
        try:
            cad = float(input("Please enter the amount of CAD to convert: "))
        except ValueError:
            cad = -1
        while cad < 0:
            try:
                cad = float(input("Illegal input. Please try again: "))
            except ValueError:
                cad = -1
        # Perform the conversion
        usd = cad * CAD_TO_USD

    # Case #2 -- user enters EUR -> USD
    elif convertType == "EUR":
        # Use an input validation loop
        try:
            eur = float(input("Please enter the amount of EUR to convert: "))
        except ValueError:
            eur = -1
        while eur < 0:
            try:
                eur = float(input("Illegal input. Please try again: "))
            except ValueError:
                eur = -1
        # Perform the conversion
        usd = eur * EUR_TO_USD

    # Case #3 -- user enters GBP -> USD
    elif convertType == "GBP":
        # Use an input validation loop
        try:
            gbp = float(input("Please enter the amount of GBP to convert: "))
        except ValueError:
            gbp = -1
        while gbp < 0:
            try:
                gbp = float(input("Illegal input. Please try again: "))
            except ValueError:
                gbp = -1
        # Perform the conversion
        usd = gbp * GBP_TO_USD

    # Case #4 -- user enters "q" to quit
    elif convertType.upper()[0] == "Q":
        go = False
        usd = -1.0

    # Case #5 -- bad input
    else:
        print("Error: Input was not on the list (CAD/EUR/GBP)")
        usd = -1.0
  
    # If usd is negative, don't print anything
    if usd > 0:
        print(f"The amount in USD is: {usd:.2f}")

# Goodbye message
print("Thank-you for using my currency converter. Goodbye!")
