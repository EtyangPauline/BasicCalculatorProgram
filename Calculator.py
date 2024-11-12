# Basic Calculator Program

# Prompt the user to input the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to input the second number
num2 = float(input("Enter the second number: "))

# Prompt the user to input the operation (+, -, *, or /)
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
