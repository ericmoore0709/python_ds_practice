def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    frequencies_num1 = dict()
    frequencies_num2 = dict()

    for digit in list(str(num1)):
        if (frequencies_num1.get(digit)):
            frequencies_num1[digit] += 1
        else:
            frequencies_num1[digit] = 1

    for digit in list(str(num2)):
        if (frequencies_num2.get(digit)):
            frequencies_num2[digit] += 1
        else:
            frequencies_num2[digit] = 1

    return (frequencies_num1 == frequencies_num2)