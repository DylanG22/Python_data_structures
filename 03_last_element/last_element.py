def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # length = len(lst)
    # if length >= 1:
    #     return lst[length - 1]
    
    if len(lst) >= 1:
        return lst[-1]


