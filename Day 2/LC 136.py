# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1), as we are using a constant amount of space for the variable result.
# The XOR operation is used here because it has the property that a ^ a = 0 and 
# a ^ 0 = a, which means that when we XOR all the numbers together.
# This will cancel out all the numbers that appear twice, leaving only the single number.
# This solution is efficient and meets the problem's requirements for linear runtime complexity and constant space usage.