def truncate(phrase, n):
    """Return truncated-at-n-chars version of phrase."""
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    if len(phrase) <= n:
        return phrase
    
    return phrase[:n - 3] + '...'
