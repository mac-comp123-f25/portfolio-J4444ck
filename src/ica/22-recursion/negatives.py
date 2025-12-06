def count_negatives(nums):
    if nums == []:
        return 0
    first = nums[0]
    rest = nums[1:]
    if first < 0:
        return 1 + count_negatives(rest)
    else:
        return count_negatives(rest)
