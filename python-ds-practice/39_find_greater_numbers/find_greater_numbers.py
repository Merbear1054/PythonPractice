def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number."""
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count
