import math
import logging
#viva
# create log file
logging.basicConfig(filename="calculator.log", level=logging.INFO)

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Log (ln)")
    print("4. Power (x^y)")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        x = float(input("Enter number: "))
        result = math.sqrt(x)
        print("Result:", result)
        logging.info(f"Square root of {x} = {result}")

    elif choice == "2":
        x = int(input("Enter number: "))
        result = math.factorial(x)
        print("Result:", result)
        logging.info(f"Factorial of {x} = {result}")

    elif choice == "3":
        x = float(input("Enter number: "))
        result = math.log(x)
        print("Result:", result)
        logging.info(f"Natural log of {x} = {result}")

    elif choice == "4":
        x = float(input("Enter base: "))
        y = float(input("Enter power: "))
        result = math.pow(x, y)
        print("Result:", result)
        logging.info(f"{x} power {y} = {result}")

    elif choice == "5":
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice")


