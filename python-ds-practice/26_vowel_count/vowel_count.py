def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive."""
    phrase = phrase.lower()
    vowels = 'aeiou'
    count = {}

    for char in phrase:
        if char in vowels:
            count[char] = count.get(char, 0) + 1

    return count
