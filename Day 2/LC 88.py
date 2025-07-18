# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        for z in range(m+n-1, -1, -1):
            if i < 0:
                nums1[z] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[z] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[z] = nums1[i]
                i -= 1
            else:
                nums1[z] = nums2[j]
                j -= 1
        return nums1


        