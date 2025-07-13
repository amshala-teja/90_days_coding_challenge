# 1584. Min Cost to Connect All Points

# You are given an array points representing integer coordinates of some points on a 2D-plane, 
# where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: 
# |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. 
# All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

import heapq
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        total_cost = 0
        seen = set()
        min_heap = [(0, 0)]

        while len(seen) < n:
            d, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += d
            xi, yi = points[i]
            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_dist, j))
        return total_cost