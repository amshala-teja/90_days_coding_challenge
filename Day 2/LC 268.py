# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = (n*(n+1))//2
        actual_sum = sum(nums)
        missing_number = total_sum - actual_sum
        return missing_number

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1), as we are using a constant amount of space for variables

# we can also solve by sorting the array where the time complexity will be O(nlogn) and space complexity will be O(1)
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
