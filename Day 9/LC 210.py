# 210. Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#  You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
# return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So the correct course order is [0,1].

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        g = defaultdict(list)
        for u, v in prerequisites:
            g[u].append(v)
        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited]*numCourses

        
        def dfs(i):
            if states[i] == visiting:
                return False
            elif states[i] == visited:
                return True
            states[i] = visiting
            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = visited
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
