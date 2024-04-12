#S.C. = O(1)
#T.C. = O(n)
def merge(nums1, m, nums2, n):
    idx = n + m - 1
    i = m -1
    j = n - 1

    while i>-1 and j>-1:
        if nums1[i] >= nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
            idx -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1