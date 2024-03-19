def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase:str = ""
    for c in phrase:
        if (c.lower() == to_swap.lower()):
            new_phrase += c.upper() if c.islower() else c.lower()
        else:
            new_phrase += c
    return new_phrase
