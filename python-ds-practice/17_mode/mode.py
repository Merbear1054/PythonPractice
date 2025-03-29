def mode(nums):
    """Return most-common number in list."""
    from collections import Counter
    counts = Counter(nums)
    return counts.most_common(1)[0][0]
