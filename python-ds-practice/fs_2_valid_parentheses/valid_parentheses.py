def valid_parentheses(parens):
    """Are the parentheses validly balanced?"""
    balance = 0
    for char in parens:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0
