import math  # Import the math module for mathematical operations

# Define functions for basic mathematical operations

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square_root(x):
    return math.sqrt(x)

def exponentiation(x, y):
    return x ** y

def factorial(x):
    return math.factorial(x)

def square(x):
    return x ** 2

def modulus(x, y):
    return x % y

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def logarithm(x, base):
    if base == 1:
        return "Error! Base cannot be 1."
    return math.log(x, base)

# Print available operations for the user

print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Exponentiation")
print("7. Factorial")
print("8. Square of a number")
print("9. Modulus")
print("10. Sine")
print("11. Cosine")
print("12. Tangent")
print("13. Logarithm")

# Start a loop to allow the user to perform multiple operations

while True:
    # Ask the user to choose an operation
    choice = input("Choose the operation you want to perform (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'):
        # Perform the chosen operation
        if choice in ('1', '2', '3', '4', '6', '9'):
            # For operations that require two numbers
            number1 = float(input("Enter the first number: "))
            if choice == '6':
                exponent_value = float(input("Enter the exponent value: "))
                print("Result:", exponentiation(number1, exponent_value))
            else:
                number2 = float(input("Enter the second number: "))
                if choice == '1':
                    print("Result:", addition(number1, number2))
                elif choice == '2':
                    print("Result:", subtraction(number1, number2))
                elif choice == '3':
                    print("Result:", multiplication(number1, number2))
                elif choice == '4':
                    print("Result:", division(number1, number2))
                elif choice == '9':
                    print("Result:", modulus(number1, number2))
        elif choice == '5':
            # For square root operation
            number = float(input("Enter the number to find its square root: "))
            print("Result:", square_root(number))
        elif choice == '7':
            # For factorial operation
            number = float(input("Enter the number to find its factorial: "))
            print("Result:", factorial(int(number)))
        elif choice == '8':
            # For finding square of a number
            number = float(input("Enter the number to find its square: "))
            print("Result:", square(number))
        elif choice in ('10', '11', '12'):
            # For trigonometric functions
            angle = float(input("Enter the angle in degrees: "))
            angle_rad = math.radians(angle)
            if choice == '10':
                print("Result:", sine(angle_rad))
            elif choice == '11':
                print("Result:", cosine(angle_rad))
            elif choice == '12':
                print("Result:", tangent(angle_rad))
        elif choice == '13':
            # For logarithmic function
            number = float(input("Enter the number for logarithm: "))
            base = float(input("Enter the base of the logarithm: "))
            print("Result:", logarithm(number, base))
    else:
        print("Invalid input!")  # Notify user if input is invalid

    # Ask the user if they want to perform another operation
    proceed = input("Do you want to perform another operation? (Y/N): ")
    if proceed.upper() != 'Y':
        break  # Exit the loop if user chooses not to continue
