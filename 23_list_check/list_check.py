def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    res = True
    for el in lst:
        if not isinstance(el,list):
            res = False
    
    return res
        
