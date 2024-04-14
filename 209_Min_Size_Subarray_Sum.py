#T.C. = O(n)
#S.C = O(1)
def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_diff = float('inf')
    diff = float('inf')
    idx0 = 0
    idx1 = 0
    s0 = 0
    s1 = 0
    for n in nums:
        s1 += n
        idx1 += 1
        while s1-s0 >= target:
            s0 += nums[idx0]
            idx0 += 1
            diff = idx1 - idx0 + 1
        if diff < min_diff:
            min_diff = diff
    if min_diff == float('inf'):
        return 0
    else:
        return min_diff


print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
