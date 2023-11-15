def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factor = 1
    res = []
    if num % 2 == 0:
        while factor <= num:
            if num % factor == 0:
                res.append[factor]
            factor += 1
    else: 
        while factor <= num:
            if num % factor == 0:
                res.append[factor]
            factor += 2

    return res