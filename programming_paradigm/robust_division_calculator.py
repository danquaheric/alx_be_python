# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide numerator by denominator.
    Handles:
      - non-numeric input: prints appropriate error message
      - division by zero: prints appropriate error message
    Returns:
      - On success: a string with the result
      - On error: a string with error message
    """
    try:
        # attempt converting inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
