def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase."""
    swapped = ''
    for char in phrase:
        if char.lower() == to_swap.lower():
            swapped += char.swapcase()
        else:
            swapped += char
    return swapped
