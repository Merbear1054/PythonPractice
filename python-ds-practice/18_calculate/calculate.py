def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, (possibly truncating) & returning w/msg."""
    
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        return None

    if make_int:
        result = int(result)

    return f"{message} {result}"

