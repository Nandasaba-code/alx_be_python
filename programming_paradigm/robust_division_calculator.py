
#Perform division safely, handling errors like zero division and invalid input.

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers and handles:
    - Division by zero
    - Non-numeric inputs
    """
    try:
        # Convert inputs to float (this may raise ValueError if not numeric)
        num = float(numerator)
        den = float(denominator)

        # Attempt the division (this may raise ZeroDivisionError)
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Runs if denominator is zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Runs if input cannot be converted to float
        return "Error: Please enter numeric values only."
