def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those."""
    return {key: values[i] if i < len(values) else None for i, key in enumerate(keys)}