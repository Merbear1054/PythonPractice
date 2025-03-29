def partition(lst, fn):
    """Partition lst by predicate."""
    true_list = [item for item in lst if fn(item)]
    false_list = [item for item in lst if not fn(item)]
    return [true_list, false_list]
