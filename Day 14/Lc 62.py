# 62. Unique Paths

# There is a robot on an m x n grid. The robot is initially located at the top-left corner 
# (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths
#  that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # this is the recursive solution and doesn't pass the test cases
        #which has TC = O(2pow(n*m)) and SC = O(m*n)
        def paths(i, j):
            if  i == j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                return paths(i, j-1) + paths(i-1, j)
        return paths(m-1, n-1)
        # we can use top - down/memoization here:
        memo = {
            (0, 0) :1, 
        }
        def paths(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                value = paths(i, j-1) + paths(i-1, j)
                memo[(i, j)] = value
                return memo[(i, j)]
        return paths(m-1, n-1)
        
        # using tabulation or bottom up approach

        dp = []
        for _ in range(m):
            dp.append([0]*n)
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                val = 0
                if i > 0:
                    val += dp[i-1][j]
                if j > 0:
                    val += dp[i][j-1]
                dp[i][j] = val
        return dp[m-1][n-1]