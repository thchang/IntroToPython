# Declare secret usernames
SECRET_USERNAME = "zarkerberg11"
SECRET_PASSWORD = "myspace99"

# Get user input (name, username, and password)
fullName = input("Please enter your full name: ")
userName = input("Please enter your user name: ")
password = input("Please enter your password: ")

# Check username and password using if + and operator
if userName == SECRET_USERNAME and password == SECRET_PASSWORD:
    # Print a customized welcome message, by splitting name into first/last
    print("Successful login: Welcome to BookFace " + fullName.split()[0])
else:
    print("Could not verify your credentials")
