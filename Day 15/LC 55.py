# 55. Jump Game
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. 
# Its maximum jump length is 0, which makes it impossible to reach the last index.
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # this is top down / memoization method. It doesn't pass the 
        # test cases as TC = O(n**2), SC = O(n)
        n = len(nums)
        memo = {n-1 : True}
        def can_reach(i):
            if i in memo:
                return memo[i]
            for jump in range(1, nums[i]+1):
                if can_reach(i+jump):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return can_reach(0)
        # Hence we go for greedy approach here.
        #Lets say our target if the end and when added with index i, 
        # it should reach the beginning of the array. then its true
        n = len(nums)
        target = n-1
        for i in range(n-1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
        return target == 0

        