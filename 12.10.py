#Question no 10:-
import math
import random

while True:
    print("\n--- Smart Calculator & Data Manager ---")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            print("1.Addition")
            print("2.Subtraction")
            print("3.Multiplication")
            print("4.Division")

            op = input("Choose operation: ")

            if op == "1":
                print("Result:", a + b)
            elif op == "2":
                print("Result:", a - b)
            elif op == "3":
                print("Result:", a * b)
            elif op == "4":
                print("Result:", a / b)
            else:
                print("Invalid operation")

        except ValueError:
            print("Please enter numbers only")
        except ZeroDivisionError:
            print("Cannot divide by zero")

    elif choice == "2":
        try:
            num = float(input("Enter number: "))

            print("Square root:", math.sqrt(num))
            print("Square:", math.pow(num, 2))
            print("Factorial:", math.factorial(int(num)))

        except ValueError:
            print("Invalid value for calculation")

    elif choice == "3":
        try:
            n = int(input("How many random numbers: "))

            for i in range(n):
                print(random.randint(1, 100))

        except ValueError:
            print("Enter a valid number")

    elif choice == "4":
        print("Calculator closed")
        break

    else:
        print("Invalid choice")