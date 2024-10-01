# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform: 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    float: The result of the arithmetic operation.
    str: A message indicating an invalid operation or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"









# main.py

from arithmetic_operations import perform_operation

def main():
    # Test cases for the arithmetic operations
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    result = perform_operation(num1, num2, operation)

    if isinstance(result, str):  # If result is an error message
        print(result)
    else:
        print(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()
