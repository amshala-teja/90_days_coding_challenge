# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
# return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, 
# an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            left = nums[m - 1] if m - 1 >= 0 else float('-inf')
            right = nums[m + 1] if m + 1 < n else float('-inf')
            if left < nums[m] and nums[m] > right:
                return m
            elif left < nums[m] < right:
                l = m+1
            else:
                r = m-1
        return -1
    

# Logic: 

# We use binary search to find a peak element.
# A peak element is defined as nums[i] > nums[i - 1] and nums[i] > nums[i + 1].
    # 1. We initialize the search boundaries with l = 0 and r = n - 1.
    # 2. In each iteration, we pick the middle index m.
    # 3. We safely get the left and right neighbor values.
        # - If m is at the boundary, we treat out-of-bound neighbors as -infinity.
    # 4. If nums[m] is greater than both neighbors, we found a peak.
    # 5. If the right neighbor is greater, it means there is at least one peak on the right side.
    # 6. Otherwise, there is at least one peak on the left side.
    # 7. Binary search ensures O(log n) time complexity.