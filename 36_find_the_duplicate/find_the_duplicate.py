def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    indx_1 = 0
    indx_2 = 1

    nums = sorted(nums)

    ptr_1 = nums[indx_1]
    ptr_2 = nums[indx_2]
    
    

    while ptr_1 != ptr_2:
        
        indx_1+=1
        indx_2+=1

        if indx_2 == len(nums):
            return None

        ptr_1 = nums[indx_1]
        ptr_2 = nums[indx_2]
    
    return ptr_1