# Develop a simple calculator that can perform basic operations like addition, subtraction, multiplication, and division.
def simple_calculator():
    print("\n ------------------------------ SIMPLE CALCULATOR MENU ------------------------------")
    print("\nPress 1 for ADDITION.")
    print("Press 2 for SUBTRACTION.")
    print("Press 3 for MULTIPLICATION.")
    print("Press 4 for DIVISION.")
    print("Press 5 to EXIT.")

def user_choice():
    return input("Enter your choice: ")

def addition_(num1, num2):
    sum = num1 + num2
    print(f"THE SUM OF YOUR ENTERED NUMBERS IS: {round(sum, 2)}")

def subtraction_(num1, num2):
    difference = num1 - num2
    print(f"THE DIFFERENCE BETWEEN YOUR ENTERED NUMBERS IS: {round(difference, 2)}")

def multiplication_(num1, num2):
    product = num1 * num2
    print(f"THE PRODUCT OF YOUR ENTERED NUMBERS IS: {round(product, 2)}")

def division_(numerator, denomenator):
    try:
        div_answer = numerator / denomenator
        print(f"THE RESULT OF {numerator} DIVIDED BY {denomenator} IS: {round(div_answer, 2)}")
    except ZeroDivisionError:
        if denomenator == 0:
            print("ERROR! A NUMBER CANNOT BE DIVIDED BY ZERO.")

def exit_menu():
    print("YOU EXIT THE CALCULATOR.")

while True:
    simple_calculator()
    choice = user_choice()

    if choice in ("1", "2", "3", "4"):
        while True:
            try:
                num1 = float(input("Enter your First Number: "))
                num2 = float(input("Enter your Second Number: "))
                break
            except ValueError:
                print("PLEASE ENTER A NUMERIC VALUE.")
    
    if choice == "1":
        addition_(num1, num2)
    elif choice == "2":
        subtraction_(num1, num2)
    elif choice == "3":
        multiplication_(num1, num2)
    elif choice == "4":
        division_(num1, num2)
    elif choice == "5":
        exit_menu()
        break
    else:
        print("PLEASE MAKE A VALID CHOICE.")