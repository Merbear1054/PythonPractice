def friend_date(a, b):
    """Do two friends have any hobbies in common?"""
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])
    return bool(hobbies_a & hobbies_b)
