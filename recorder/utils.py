def diff_states(prev, curr):
    """
    Compare two locals() dictionaries and return only changed variables.
    """
    return {
        k: (prev.get(k), curr.get(k))
        for k in curr
        if prev.get(k) != curr.get(k)
    }
