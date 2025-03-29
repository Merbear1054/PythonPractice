def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal."""
    seen = set()
    for num in nums:
        complement = goal - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return ()

