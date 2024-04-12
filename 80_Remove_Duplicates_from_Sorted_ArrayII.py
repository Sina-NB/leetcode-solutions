def removeDuplicates(self, nums: list[int]) -> int:
    seen = {}
    index = 0
    l = len(nums)

    for i in range(l):
        if seen.get(nums[i], 0) < 2:
            nums[index] = nums[i]
            seen[nums[i]] = seen.get(nums[i], 0) + 1
            index += 1
    
    return index