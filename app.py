def multiply(a, b):
    # Core function for multiplication
    return a * b

def divide(a, b):
    # Core function for division, prevents division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
