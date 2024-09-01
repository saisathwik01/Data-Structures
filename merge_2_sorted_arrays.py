# Question: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# CODE:

# O(m+n)
def merge(nums1,nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    m=len(nums1)
    n=len(nums2)
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# O(n1)
def merge(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    i = 0
    k = 0

    while i < n1 and k < n2:
        if nums1[i] == 0:
            nums1[i] = nums2[k]
            k += 1
        i += 1

    return nums1