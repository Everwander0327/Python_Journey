# Import the 'process' module where the core calculator functions are implemented
import process
# Import colorama for colored console output
from colorama import Fore, Style, init
# Initialize colorama to enable ANSI color codes in terminal
init()
def add(num1, num2):
    """
    Calculate and display the sum of two numbers with green text.

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    """
    print(
        "\nThe sum of " + str(num1) + " and " + str(num2) + " is " +
        Fore.GREEN + str(process.add(num1, num2)) + Style.RESET_ALL
    )


def minus(num1, num2):
    """
    Calculate and display the difference of two numbers with red text.

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    """
    print(
        "The difference of " + str(num1) + " and " + str(num2) + " is " +
        Fore.RED + str(process.subtract(num1, num2)) + Style.RESET_ALL
    )


def times(num1, num2):
    """
    Calculate and display the product of two numbers with yellow text.

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    """
    print(
        "The product of " + str(num1) + " and " + str(num2) + " is " +
        Fore.YELLOW + str(process.multiply(num1, num2)) + Style.RESET_ALL
    )

def divide(num1, num2):
    """
    Calculate and display the quotient of two numbers with magenta text.
    Args:
        num1 (int/float): Dividend
        num2 (int/float): Divisor
    """
    print(
        "The quotient of " + str(num1) + " and " + str(num2) + " is " +
        Fore.MAGENTA + str(process.divide(num1, num2)) + Style.RESET_ALL
    )