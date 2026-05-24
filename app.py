def add(a, b):
    """Return addition result."""
    return a + b


def subtract(a, b):
    """Return subtraction result."""
    return a - b


def multiply(a, b):
    """Return multiplication result."""
    return a * b


def divide(a, b):
    """Return division result."""
    if b == 0:
        return "Cannot divide by zero"

    return a / b


if __name__ == "__main__":
    print("Calculator App")
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(6, 7))
    print(divide(8, 2))
