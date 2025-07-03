# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findFirst(nums, target):
            n = len(nums)
            l, r = 0, n-1
            first = -1
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    first = m
                    r = m-1
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return first
        def findLast(nums, target):
            l, r = 0, len(nums)-1
            last = -1
            while l<= r:
                m = (l+r)//2
                if nums[m] == target:
                    last = m
                    l = m+1
                elif  nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return last
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]


# Logic:
# - Use binary search twice:
#     1. First to find the first occurrence.
#     2. Second to find the last occurrence.

# Time Complexity: O(log n)
# Space Complexity: O(1)

        