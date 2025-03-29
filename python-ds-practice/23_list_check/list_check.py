def list_check(lst):
    """Are all items in lst a list?"""
    return all(isinstance(item, list) for item in lst)

