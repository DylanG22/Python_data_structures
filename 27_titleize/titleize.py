def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = list(phrase.lower())
    res = []

    for i in range(len(lst)):
        if len(res) == 0:
            res.append(lst[i].upper())
        if lst[i-1]== ' ':
            res.append(lst[i].upper())
        else:
            res.append(lst[i])
    
    return ''.join(res)