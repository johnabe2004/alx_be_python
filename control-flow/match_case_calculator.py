num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Choose the operation (+, -, *, /): ") 
match operation:
        case '+':
            result = num1 + num2
            print(f"The result is: {result}")
        case '-':
            result = num1 - num2
            print(f"The result is: {result}")
        case '*':
            result = num1 * num2
            print(f"The result is: {result}")
        case '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is: {result}")
        case _:
            print("\nInvalid operation. Please select a valid operator (+, -, *, /).")
