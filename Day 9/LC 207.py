# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 
# 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)

        for u,v in prerequisites:
            g[u].append(v)
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses
        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            states[node] = visiting
            for nei_node in g[node]:
                if not dfs(nei_node):
                    return False
            states[node] = visited
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True