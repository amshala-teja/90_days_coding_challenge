# 994. Rotting Oranges
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
# If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
# because rotting only happens 4-directionally.

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        empty, fresh, rotten = 0, 1, 2
        num_fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    q.append((i, j))
                elif grid[i][j] == fresh:
                    num_fresh += 1
        if num_fresh == 0:
            return 0
        
        num_minutes = -1
        while q:
            q_size = len(q)
            num_minutes += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for r, c in [(i, j+1), (i+1,j), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        num_fresh -= 1
                        q.append((r,c ))
        if num_fresh == 0:
            return num_minutes
        else:
            return -1