def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letterDict = dict()

    for c in phrase:
        if (letterDict.get(c)):
            letterDict[c] = letterDict.get(c) + 1
        else:
            letterDict[c] = 1
    
    return letterDict