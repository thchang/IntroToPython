# Declare secret usernames
SECRET_USERNAME = "zarkerberg11"
SECRET_PASSWORD = "myspace99"

# Get user input (username and password)
userName = input("Please enter your user name: ")
password = input("Please enter your password: ")

# Check username and password using if + and operator
if userName == SECRET_USERNAME and password == SECRET_PASSWORD:
    print("Successful login: Welcome to BookFace")
else:
    print("Could not verify your credentials")
