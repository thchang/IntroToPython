# Define all functions for future usage BEFORE writing any code

def print_instructions():
    print("Welcome to the guessing game!")
    print("Instructions:")
    print("Pick a number between 0 and 9")
    print("Don't tell anyone what you picked!")
    return

def print_blank_lines(nlines=10):
    for i in range(nlines):
        print()
    return

def get_player_input(pname):
    userInput = -1
    while userInput < 0 or userInput > 9:
        try:
            userInput = int(input(f"{pname}: enter your pick here: "))
        except:
            userInput = -1
    return userInput

# Play the game by calling the 3 functions defined above
print_blank_lines()
print_instructions()
print_blank_lines()
playerOneNumber = get_player_input("Player 1")
print_blank_lines(nlines=50)
print_instructions()
print_blank_lines()
playerTwoNumber = get_player_input("Player 2")
print_blank_lines(nlines=20)

# Print final output
if playerTwoNumber == playerOneNumber:
    print("Player 2 wins!", end="\n")
else:
    print("Player 1 wins!", end="\n")
# Print some final blank lines
print_blank_lines()
