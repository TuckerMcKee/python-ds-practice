def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest_count = 0
    mode = None
    for i in range(len(nums)):
        if nums.count(nums[i]) > highest_count:
            highest_count = nums.count(nums[i])
            mode = nums[i]
    return mode