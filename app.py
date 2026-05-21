"""Simple calculator module with basic arithmetic operations."""


def add(a, b):
    """Add two numbers and return the sum."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first and return the difference."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the product."""
    return a * b


def divide(a, b):
    """Divide the first number by the second and return the quotient."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation, num1, num2):
    """Perform a calculation based on the given operation."""
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    return result


if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)

    result1 = calculate('add', 10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calculate('multiply', 7, 3)
    print(f"7 * 3 = {result2}")

    print("Calculator completed successfully!")