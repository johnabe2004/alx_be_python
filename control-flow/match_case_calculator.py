num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Enter the operation symbol (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print("The result of", num1 ,"+", num2,"is:", result)
    case "-":
        result = num1 - num2
        print("The result of", num1 ,"-", num2, "is:", result)
    case "*":
        result = num1 * num2
        print("The result of", num1, "*", num2,"is:", result)
    case "/":
        if num2 != 0:
            result = num1 / num2
            print ("The result of", num1," /", num2,"is:", result)
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid operation selected. Please choose one of (+, -, *, /)
