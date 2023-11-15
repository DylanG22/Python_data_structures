def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse = ''
    for let in phrase:
        reverse = let + reverse
    
    return reverse

