def two_sum(nums, target):
    nums_dict = {}

    # Populate hash map
    for idx, num in enumerate(nums):
        nums_dict[num] = idx

    # Find answer
    for num, idx in nums_dict.items():
        if nums_dict.get(target - num):
            return [idx, nums_dict[target - num]]

    return "You promised!"
