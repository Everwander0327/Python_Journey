def add(num1, num2):
    """
    Return the sum of two numbers.
    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    Returns:
        int/float: Sum of num1 and num2
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Return the difference between two numbers.
    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    Returns:
        int/float: Difference (num1 - num2)
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Return the product of two numbers.
    Args:
        num1 (int/float): First number
        num2 (int/float): Second number
    Returns:
        int/float: Product of num1 and num2
    """
    return num1 * num2

def divide(num1, num2):
    """
    Return the quotient of two numbers.
    Args:
        num1 (int/float): Dividend
        num2 (int/float): Divisor
    Returns:
        float or str: Quotient of num1 divided by num2 or an error message if dividing by zero
    """
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2