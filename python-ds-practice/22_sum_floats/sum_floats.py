def sum_floats(nums):
    """Return sum of floating point numbers in nums."""
    return sum(num for num in nums if isinstance(num, float))

