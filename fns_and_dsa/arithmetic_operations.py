# arithmetic_operations

def perform_operation(num1, num2, operation):
    """
    A warm and practical function that handles basic arithmetic operations.

    Parameters:
    - num1 (float): The first number entered by the user.
    - num2 (float): The second number entered by the user.
    - operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
    - The result of the operation or a helpful message if something went wrong.
    """

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return "Oops! Division by zero is undefined. Please try another number."
        return num1 / num2

    else:
        return "Invalid operation. Please choose from: add, subtract, multiply, divide."
