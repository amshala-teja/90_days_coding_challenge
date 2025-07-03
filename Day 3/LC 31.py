# 31. Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of 
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the sorted container. 
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.




class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Logic:
        # 1. Traverse from right to left to find the first decreasing element (pivot).
        # 2. If such an element is found:
        #     a. Traverse from right to left again to find the next larger element.
        #     b. Swap them.
        # 3. Reverse the subarray to the right of the pivot to get the next smallest lexicographical order.
        
        # Time Complexity: O(n)
        #     - One pass to find the pivot: O(n)
        #     - One pass to find the next larger element: O(n) in worst case
        #     - One pass to reverse the suffix: O(n)
        #     - Total: O(n)
            
        # Space Complexity: O(1)
        #     - In-place swaps and reversals; no extra space is used.