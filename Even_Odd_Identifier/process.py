from colorama import Fore, Style, init
init()  # Enable colorama

def evenodd(number):
    """Check if a number is even or odd and display it with color."""
    if number % 2 == 0:
        # Display even numbers in yellow
        print(f"{Fore.YELLOW}{number}{Style.RESET_ALL} is Even")
    else:
        # Display odd numbers in magenta
        print(f"{Fore.MAGENTA}{number}{Style.RESET_ALL} is Odd")