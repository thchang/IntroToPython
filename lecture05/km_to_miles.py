# Tyler Chang
# CIS 2531 Sample Script
# Converts 1 km into miles and prints the result

# input
km = 1

# compute the conversion
m = km * 1000
cm = m * 100 # this line converts meters to centimeters
#print(cm)
inch = cm / 2.54
#print(inch)
ft = inch / 12
#print(ft)
mi = ft / 5280

# output
print(mi)
