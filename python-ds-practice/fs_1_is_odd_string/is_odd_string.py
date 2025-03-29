def is_odd_string(word):
    """Is the sum of the character-positions odd?"""
    total = sum(ord(char.lower()) - ord('a') + 1 for char in word)
    return total % 2 == 1
