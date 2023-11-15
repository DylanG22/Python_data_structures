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
    word_list = []
    res = True
    for letter in phrase.lower():
        if letter != ' ':
            word_list.append(letter)
    l = len(word_list) - 1
    for i in range(len(word_list)):
        if word_list[i] != word_list[l-i]:
            res = False

    return res

