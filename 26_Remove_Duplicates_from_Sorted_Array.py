# S.C. = O(n)
# T.C. = O(n)
def removeDuplicates(nums: list[int]) -> int:
    seen = set()
    index = 0
    l = len(nums)

    for i in range(l):
        if nums[i] not in seen:
            nums[index] = nums[i]
            seen.add(nums[i])
            index += 1
    
    return index