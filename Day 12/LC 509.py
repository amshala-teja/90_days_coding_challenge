# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. 
# That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # recursive approach:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-2) + self.fib(n-1) 
        # top down approach using Memo:
        memo = {0:0, 1:1}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)
        # bottom up approach using tabulation:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        # optimized approach:
        prev = 0
        curr = 1
        for i in range(2, n+1):
            prev, curr = curr, prev+curr
        return curr
        # golden ratio method:
        golden_ratio = (1+(5**0.5))/2
        return int(round((golden_ratio**n)/(5**0.5)))