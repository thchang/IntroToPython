# A long, complicated calculation split over 2 lines, using line continuation
x = (5 * 6) ** 2 - \
    10 / (2 ** (3 + 5)) + 67.7
print(x) # Output type is promoted to float

# A long, complicated calculation split over 2 lines, using parentheses
x = ((5 * 6) ** 2 -
     10 / (2 ** (3 + 5)) + 67.7)
print(x) # Output type is promoted to float
