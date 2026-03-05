# main.py - Simple Calculator with color output

import result
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init()

# Greet the user
username = input("Hello! Please enter your name: ")
print(f"\nHi {Fore.BLUE}{username}{Style.RESET_ALL}, welcome to Simple Calculator!\n")


def get_numbers():
    """
    Prompt the user to enter two integers.
    Repeats until valid integers are provided.

    Returns:
        tuple: Two integers entered by the user
    """
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")


# Get validated user input
num1, num2 = get_numbers()

# Perform calculations and display results
result.add(num1, num2)
result.minus(num1, num2)
result.times(num1, num2)
result.divide(num1, num2)