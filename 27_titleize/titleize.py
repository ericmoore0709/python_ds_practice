def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return_words = []
    for x in phrase.split(" "):
        return_words.append(x[0].upper() + x[1:].lower())
    
    return ' '.join(return_words)
