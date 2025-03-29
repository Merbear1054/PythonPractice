def reverse_vowels(s):
    """Reverse vowels in a string."""
    vowels = set('aeiouAEIOU')
    s = list(s)
    
    # Get the indexes of all vowels
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)
