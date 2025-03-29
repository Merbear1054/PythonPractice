def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?"""
    if isinstance(collection, dict):
        return sought in collection.values()
    
    if isinstance(collection, (list, str, tuple)) and start is not None:
        return sought in collection[start:]
    
    return sought in collection
