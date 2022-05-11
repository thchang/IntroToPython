# Create a dict of username (key) and password (value) pairs
USER_DATABASE = {"zarkerberg11": "myspace99",
                 "jeffyjeffb": "wallmart_00",
                 "JeveStobs": "macro-hard-123"}

# Get full name, username, and password as user inputs
fullName = input("Please enter your full name: ")
userName = input("Please enter your user name: ")
password = input("Please enter your password: ")

# Check if userName/password are in the dict's keys/values list
if userName in USER_DATABASE.keys() and password == USER_DATABASE[userName]:
    print("Successful login: Welcome to BookFace " + fullName.split()[0])
else:
    print("Could not verify your credentials")
