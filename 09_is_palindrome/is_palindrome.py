def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    length = len(phrase) - 1
    reverse = phrase[length:0:-1]
    idx = 0
    is_pal = True

    while idx >= length :
        phrase_idx = idx
        reverse_idx = idx
        if phrase(idx) == ' ':
            phrase_idx += 1
        if reverse(idx) == ' ':
            reverse_idx += 1

        if phrase.lower()[phrase_idx] != reverse.lower()[reverse_idx]:
            is_pal = False
        
    return is_pal
