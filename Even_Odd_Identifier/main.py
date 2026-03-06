# Import the module containing the odd/even logic
import process

# Import colorama for colored text in the terminal
from colorama import Fore, Style, init
init()  # Enable colorama

def user():
    """Prompt the user to enter their name."""
    name = str(input("Please Enter your name: "))
    return name

def greet():
    """Display a welcome message with the user's name highlighted."""
    print(f"Welcome to odd even number checker {Fore.BLUE}{username}{Style.RESET_ALL}")

def numchoice():
    """Prompt for a number, validate input, and check if it's odd or even."""
    while True:
        number = input("\nPlease enter a number to start guessing: ")
        try:
            number = int(number)  # Ensure input is numeric
            process.evenodd(number)  # Call the core logic
            break
        except:
            # Show error if input is invalid
            print(f"{Fore.RED}Error! Please Enter a Number only{Style.RESET_ALL}")

# Main program execution
username = user()  # Get the user's name
greet()            # Show welcome message
numchoice()        # Run number input and odd/even check