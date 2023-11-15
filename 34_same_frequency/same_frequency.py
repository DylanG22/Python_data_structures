def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_dict = {}
    num2_dict = {}

    for digit in f'{num1}':
        if digit in num1_dict:
            num1_dict[digit] = num1_dict[digit] + 1
        else:
            num1_dict[digit] = 1
    for digit in f'{num2}':
        if digit in num2_dict:
            num2_dict[digit] = num2_dict[digit] + 1
        else:
            num2_dict[digit] = 1

    return num1_dict == num2_dict



