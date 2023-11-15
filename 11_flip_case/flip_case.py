def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_word = []
    for letter in phrase:
        if(to_swap == to_swap.upper()):
            lower = to_swap.lower()
            upper = to_swap
        else:
            lower = to_swap
            upper = to_swap.upper()

        if letter == lower :
            swapped_word.append(letter.upper())
        elif letter == upper:
            swapped_word.append(letter.lower())
        else:
            swapped_word.append(letter)

    return ''.join(swapped_word)