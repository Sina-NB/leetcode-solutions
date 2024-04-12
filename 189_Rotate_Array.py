# T.C. = O(n)
# S.C = O(1)
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k=k%l
    queue = []
    for i in range(k):
        queue.append(nums[i])
    
    for i in range(l):
        idx = (i+k)%l
        queue.append(nums[idx])
        nums[idx] = queue.pop(0)
    return nums

print(rotate([1,2,3,4,5,6,7], 3))  