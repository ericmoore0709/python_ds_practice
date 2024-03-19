def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum_of_first_diag = 0
    indx = 0

    while indx < len(matrix[0]):
        sum_of_first_diag += matrix[indx][indx]
        indx += 1

    sum_of_second_diag = 0
    indx = 0
    indy = len(matrix[0]) - 1

    while indx < len(matrix[0]):
        sum_of_second_diag += matrix[indx][indy]
        indx += 1
        indy -= 1

    return sum_of_first_diag + sum_of_second_diag
