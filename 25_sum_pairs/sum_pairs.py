def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    index_pairs = []
    lowest_high_index = len(nums)
    final_pair = ()
    for i in range(len(nums)):
        for x in range(i + 1, len(nums)):
            if nums[i] + nums[x] == goal:
                index_pairs.append([i,x])     
    for i in range(len(index_pairs)):
        if index_pairs[i][1] < lowest_high_index:
            lowest_high_index = index_pairs[i][1]
            final_pair = (nums[index_pairs[i][0]],nums[index_pairs[i][1]])
    return final_pair