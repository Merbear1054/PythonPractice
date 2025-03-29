def repeat(phrase, num):
    """Return phrase, repeated num times."""
    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num
