def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase."""
    count = {}
    for char in phrase:
        count[char] = count.get(char, 0) + 1
    return count
