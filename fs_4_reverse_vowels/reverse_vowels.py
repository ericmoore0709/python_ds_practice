def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = dict()
    string_builder = list(s)
    for x in range(len(s)):
        if s[x] in 'aeiouAEIOU':
            vowels[x] = s[x]

    key_list = list(vowels.keys())
    indx = len(key_list) - 1
    
    for x in range(len(s)):
        if vowels.get(x):
            string_builder[x] = vowels[key_list[indx]]
            indx -= 1
    
    return ''.join(string_builder)
