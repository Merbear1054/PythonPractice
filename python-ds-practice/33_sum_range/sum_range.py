def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end."""
    if end is None or end >= len(nums):
        end = len(nums) - 1
    return sum(nums[start:end+1])
