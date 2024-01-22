'''Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1/num2
    elif operation == "%":
        return num1 %num2
    
    else :
         return "invalid"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %): ")

# Perform the selected operation
result = calculator(num1, num2, operation)

# Display the result
print(f"Result: {result}")








