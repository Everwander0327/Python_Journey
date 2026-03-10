Data = []
UserFields = ["Name", "Age", "Gender", "Section", "Year", "Username", "Password"]

def WelcomeScreen():
    print("=" * 35)
    print("     STUDENT PORTAL SYSTEM")
    print("=" * 35)

def MainMenu():
    print("\n===== MAIN MENU =====")
    print("  [1] Login Account")
    print("  [2] Register Account")
    print("=" * 21)

def LastEntry():
    print("\n--- Last Entry ---")
    for i in Data[-1]:
        print(f"  {i}: {Data[-1][i]}")
    print("-" * 18)

def Login():
    print("\n===== LOGIN =====")
    Username = input("  Username: ")
    Password = input("  Password: ")

    for i in Data:
        if Username == i["Username"] and Password == i["Password"]:
            print("\n>>> Login Successful!")
            print(f">>> Welcome, {i['Name']}! ({i['Year']} Year, {i['Age']} yrs old)")
            break
    else:
        print(">>> !! Invalid Credentials! Try Again !!")
        Main()

def Register():
    print("\n===== REGISTRATION =====")
    users = {}
    for i in UserFields:
        users[i] = input(f"  {i}: ")
    Data.append(users)
    LastEntry()
    choice = input("\n  Add another entry? (Y/N): ").upper()
    if choice == "Y":
        Register()
    elif choice == "N":
        Main()
    else:
        print(">>> !! Invalid Input !!")
        Main()

def Main():
    MainMenu()
    choice = input("  Choice: ")
    if choice == "1":
        Login()
    elif choice == "2":
        Register()
    else:
        print(">>> !! Invalid Choice !!")
        Main()

WelcomeScreen()
Main()