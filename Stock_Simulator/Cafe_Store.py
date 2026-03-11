import os
from colorama import Fore, Back, Style, init
init(autoreset=True)  # autoreset so we don't need Style.RESET_ALL after every print


# ========================
#  CLI Helpers
# ========================

# Clears the terminal — works on both Windows (cls) and Mac/Linux (clear)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prints a dim horizontal line to separate sections
def divider():
    print(Fore.WHITE + Style.DIM + "  " + "─" * 41 + Style.RESET_ALL)

# Clears the screen and prints a branded header for each page
def header(title):
    clear()
    print()
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + f"  🐾  Neko's Cafe  —  {title:<20}" + Style.RESET_ALL)
    divider()
    print()


# ========================
#  Product Class
# ========================

class Products:
    count = 0  # Class variable — tracks how many products have been created

    # Sets up a new product with name, stock, and price
    def __init__(product, name, stock, price):
        Products.count += 1  # Increment count every time a new product is created
        product.name  = name
        product.stock = stock
        product.price = price

    # Handles product purchase — asks quantity, computes total, deducts stock
    def SellProduct(product):
        while True:
            try:
                header("Buy Products")
                print(Fore.CYAN + Style.BRIGHT + f"  Selected : {product.name}" + Style.RESET_ALL)
                print(Fore.WHITE + Style.DIM   + f"  Price    : ${product.price:.2f} each" + Style.RESET_ALL)
                print(Fore.WHITE + Style.DIM   + f"  In Stock : {product.stock} units" + Style.RESET_ALL)
                divider()

                purchase = int(input(Fore.WHITE + "\n  How many to purchase? → " + Style.RESET_ALL))

                # Prevent buying more than what's available
                if purchase > product.stock:
                    print(Fore.RED + Style.BRIGHT + f"\n  ✘  Not enough stock! Only {product.stock} left." + Style.RESET_ALL)
                    input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                    continue

                total = product.price * purchase  # Compute total cost
                product.stock = product.stock - purchase  # Deduct from stock

                print()
                divider()
                print(Fore.GREEN + Style.BRIGHT + f"  ✔  Purchase Successful!" + Style.RESET_ALL)
                print(Fore.WHITE + f"  Items bought : {purchase}x {product.name}" + Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT + f"  Total        : ${total:.2f}" + Style.RESET_ALL)
                divider()

            except ValueError:
                print(Fore.RED + Style.BRIGHT + "\n  ✘  Invalid input! Enter a number only." + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                continue

            print()
            nav = input(Fore.WHITE + Style.DIM + "  [b] Back to Main   [r] Buy Again → " + Style.RESET_ALL).strip().lower()
            if nav == "b":
                main()
                return
            elif nav == "r":
                DisplayMenu()
                return
            else:
                print(Fore.RED + "  ✘  Invalid option!" + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to continue..." + Style.RESET_ALL)

    # Handles restocking — asks how many units to add, updates stock
    def AddStock(product):
        while True:
            try:
                header("Stock Management")
                print(Fore.CYAN + Style.BRIGHT + f"  Restocking : {product.name}" + Style.RESET_ALL)
                print(Fore.WHITE + Style.DIM   + f"  Current    : {product.stock} units" + Style.RESET_ALL)
                divider()

                addedstock = int(input(Fore.WHITE + "\n  How many units to add? → " + Style.RESET_ALL))
                product.stock = product.stock + addedstock  # Add to current stock

                print()
                divider()
                print(Fore.GREEN + Style.BRIGHT + f"  ✔  Stock updated!" + Style.RESET_ALL)
                print(Fore.WHITE + f"  {product.name} now has {product.stock} units." + Style.RESET_ALL)
                divider()

            except ValueError:
                print(Fore.RED + Style.BRIGHT + "\n  ✘  Invalid input! Enter a number only." + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                continue

            print()
            nav = input(Fore.WHITE + Style.DIM + "  [b] Back to Main   [r] Restock Again → " + Style.RESET_ALL).strip().lower()
            if nav == "b":
                main()
                return
            elif nav == "r":
                DisplayStock()
                return
            else:
                print(Fore.RED + "  ✘  Invalid option!" + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to continue..." + Style.RESET_ALL)

    # Shows just the product name — used in the product list screen
    def Display(product):
        print(Fore.WHITE + Style.BRIGHT + f"  {product.name}" + Style.RESET_ALL)

    # Shows full product info for customers — flags out-of-stock items in red
    def Menu(product):
        if product.stock == 0:
            print(Fore.RED + f"  ✘  {product.name:<22}" + Style.RESET_ALL +
                  Fore.WHITE + Style.DIM + f" ${product.price:.2f}" + Style.RESET_ALL +
                  Fore.RED   + "  [ Out of Stock ]" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"  ✔  " + Style.RESET_ALL +
                  Fore.WHITE + Style.BRIGHT + f"{product.name:<22}" + Style.RESET_ALL +
                  Fore.YELLOW + Style.BRIGHT + f" ${product.price:.2f}" + Style.RESET_ALL +
                  Fore.WHITE + Style.DIM + f"  Stock: {product.stock}" + Style.RESET_ALL)

    # Displays stock levels with color-coded warnings
    # Red = critical (< 10), Yellow = low (< 25), Green = sufficient (>= 25)
    def Stock(product):
        if product.stock == 0:
            status = Fore.RED + Style.BRIGHT + f"{product.stock:>4}  [ OUT OF STOCK ]" + Style.RESET_ALL
        elif product.stock < 10:
            status = Fore.RED + Style.BRIGHT + f"{product.stock:>4}  [ CRITICAL ]" + Style.RESET_ALL
        elif product.stock < 25:
            status = Fore.YELLOW + Style.BRIGHT + f"{product.stock:>4}  [ LOW ]" + Style.RESET_ALL
        else:
            status = Fore.GREEN + Style.BRIGHT + f"{product.stock:>4}  [ OK ]" + Style.RESET_ALL

        print(Fore.WHITE + Style.BRIGHT + f"  {product.name:<22}" + Style.RESET_ALL +
              Fore.YELLOW + f" ${product.price:.2f}" + Style.RESET_ALL +
              f"  Stock: " + status)


# ========================
#  Display Functions
# ========================

# Shows all products by name only — no prices or stock info
def DisplayProduct():
    header("Product List")
    for index, i in enumerate(itemlist, 1):
        print(Fore.CYAN + f"  {index}." + Style.RESET_ALL, end=" ")
        i.Display()
    print()
    divider()
    nav = input(Fore.WHITE + Style.DIM + "\n  [b] Back to Main → " + Style.RESET_ALL).strip().lower()
    if nav == "b":
        main()
    else:
        DisplayProduct()

# Customer purchase screen — shows menu, lets user pick a product and buy it
def DisplayMenu():
    while True:
        header("Buy Products")
        for index, i in enumerate(itemlist, 1):
            print(Fore.CYAN + f"  {index}." + Style.RESET_ALL, end=" ")
            i.Menu()
        print()
        divider()

        try:
            purchase = int(input(Fore.WHITE + f"\n  Select product (1-{len(itemlist)}) → " + Style.RESET_ALL))

            # Validate range — user inputs 1-based, list is 0-based
            if purchase < 1 or purchase > len(itemlist):
                print(Fore.RED + Style.BRIGHT + f"\n  ✘  Please select between 1 and {len(itemlist)}." + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                continue

            selected = itemlist[purchase - 1]

            # Block purchase if out of stock
            if selected.stock == 0:
                print(Fore.RED + Style.BRIGHT + f"\n  ✘  '{selected.name}' is out of stock!" + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                continue

            selected.SellProduct()
            return

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\n  ✘  Invalid input! Enter a number only." + Style.RESET_ALL)
            input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)

# Admin restock screen — shows stock levels and lets admin add units to a product
def DisplayStock():
    while True:
        header("Stock Management")
        for index, i in enumerate(itemlist, 1):
            print(Fore.CYAN + f"  {index}." + Style.RESET_ALL, end=" ")
            i.Stock()
        print()
        divider()

        try:
            number = int(input(Fore.WHITE + f"\n  Select product to restock (1-{len(itemlist)}) → " + Style.RESET_ALL))

            # Validate range — user inputs 1-based, list is 0-based
            if number < 1 or number > len(itemlist):
                print(Fore.RED + Style.BRIGHT + f"\n  ✘  Please select between 1 and {len(itemlist)}." + Style.RESET_ALL)
                input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                continue

            itemlist[number - 1].AddStock()
            return

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\n  ✘  Invalid input! Enter a number only." + Style.RESET_ALL)
            input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)


# ========================
#  Objects
# ========================

# Create each product with (name, stock, price)
item1 = Products("Catpucinno", 50, 21)
item2 = Products("Ameowricanno", 40, 15)
item3 = Products("Cat Latte", 19, 17)
item4 = Products("Black Cat Coffee", 21, 10)
item5 = Products("Catberry", 8, 25)

itemlist = [item1, item2, item3, item4, item5]  # List of all products — used for looping in display functions


# ========================
#  Main Menu
# ========================

# Entry point — shows the main menu and routes to the correct screen
def main():
    while True:
        header("Main Menu")
        print(Fore.CYAN   + "  1." + Style.RESET_ALL + "  Display Products")
        print(Fore.CYAN   + "  2." + Style.RESET_ALL + "  Buy Products")
        print(Fore.YELLOW + "  3." + Style.RESET_ALL + "  Add Stocks  " + Fore.WHITE + Style.DIM + "(Admin only)" + Style.RESET_ALL)
        print(Fore.RED    + "  4." + Style.RESET_ALL + "  Exit")
        print()
        divider()

        try:
            nav = int(input(Fore.WHITE + "\n  Enter your choice → " + Style.RESET_ALL))
            match nav:
                case 1:
                    DisplayProduct()
                case 2:
                    DisplayMenu()
                case 3:
                    # Admin authentication loop
                    while True:
                        header("Admin Access")
                        passkey = input(Fore.YELLOW + "  Enter Passkey → " + Style.RESET_ALL)
                        if passkey == "0327":
                            print(Fore.GREEN + Style.BRIGHT + "\n  ✔  Access Granted!" + Style.RESET_ALL)
                            input(Fore.WHITE + Style.DIM + "\n  Press Enter to continue..." + Style.RESET_ALL)
                            DisplayStock()
                            break
                        else:
                            print(Fore.RED + Style.BRIGHT + "\n  ✘  Access Denied! Wrong passkey." + Style.RESET_ALL)
                            input(Fore.WHITE + Style.DIM + "\n  Press Enter to try again..." + Style.RESET_ALL)
                case 4:
                    clear()
                    print()
                    print(Fore.CYAN + Style.BRIGHT + "  Thanks for visiting Neko's Cafe! Goodbye! 🐾" + Style.RESET_ALL)
                    print()
                    break
                case _:
                    print(Fore.RED + Style.BRIGHT + "\n  ✘  Wrong input!" + Style.RESET_ALL)
                    input(Fore.WHITE + Style.DIM + "\n  Press Enter to continue..." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\n  ✘  Invalid input! Enter a number only." + Style.RESET_ALL)
            input(Fore.WHITE + Style.DIM + "\n  Press Enter to continue..." + Style.RESET_ALL)

main()