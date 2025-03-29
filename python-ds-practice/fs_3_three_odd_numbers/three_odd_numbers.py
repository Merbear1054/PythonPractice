def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"""
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i+1] + nums[i+2]) % 2 == 1:
            return True
    return False
