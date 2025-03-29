def is_palindrome(phrase):
    """Is phrase a palindrome?"""
    cleaned = phrase.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
