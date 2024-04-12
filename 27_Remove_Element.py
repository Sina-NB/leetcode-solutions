# S.C. = O(1)
# T.C. = O(n)
def removeElement(nums: list[int], val: int) -> int:
    index = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    
    return index