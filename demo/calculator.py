import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log10(x)


def main():
    history = []
    while True:
        print("\nAdvanced Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent (x^y)")
        print("6. Modulus (x % y)")
        print("7. Square Root")
        print("8. Sine (degrees)")
        print("9. Cosine (degrees)")
        print("10. Tangent (degrees)")
        print("11. Logarithm (base 10)")
        print("12. Show History")
        print("0. Exit")

        choice = input("Enter choice (0-12): ")

        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break
        elif choice == '12':
            print("\nCalculation History:")
            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)
            continue

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number input.")
                continue
        elif choice in ('7', '8', '9', '10', '11'):
            try:
                num1 = float(input("Enter the number: "))
            except ValueError:
                print("Invalid number input.")
                continue
        else:
            print("Invalid input")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
                output = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                output = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                output = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                output = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = exponent(num1, num2)
                output = f"{num1} ^ {num2} = {result}"
            elif choice == '6':
                result = modulus(num1, num2)
                output = f"{num1} % {num2} = {result}"
            elif choice == '7':
                result = sqrt(num1)
                output = f"sqrt({num1}) = {result}"
            elif choice == '8':
                result = sine(num1)
                output = f"sin({num1}°) = {result}"
            elif choice == '9':
                result = cosine(num1)
                output = f"cos({num1}°) = {result}"
            elif choice == '10':
                result = tangent(num1)
                output = f"tan({num1}°) = {result}"
            elif choice == '11':
                result = logarithm(num1)
                output = f"log10({num1}) = {result}"
            else:
                print("Invalid input")
                continue
            print(output)
            history.append(output)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 