def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?"""
    from collections import Counter
    return Counter(str(num1)) == Counter(str(num2))
