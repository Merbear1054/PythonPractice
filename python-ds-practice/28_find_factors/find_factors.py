def find_factors(num):
    """Find factors of num, in increasing order."""
    return [n for n in range(1, num + 1) if num % n == 0]
