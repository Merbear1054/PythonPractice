def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)."""
    unique_ages = sorted(set(ages))
    return (unique_ages[-2], unique_ages[-1])
