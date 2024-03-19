def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    indx = 0
    while indx < len(nums) - 2:
        if sum([nums[indx], nums[indx + 1], nums[indx + 2]]) % 2 != 0:
            return True
        indx+=1
    
    return False
