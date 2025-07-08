# 1971. Find if Path Exists in Graph

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
# The edges in the graph are represented as a 2D integer array edges, 
# where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
# or false otherwise.


from collections import defaultdict, deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
# DFS recursive
        if source == destination:
            return True
        D = defaultdict(list)
        for u, v in edges:
            D[u].append(v)
            D[v].append(u)

        seen = set()
        seen.add(source)
        def dfs(node):
            if node == destination:
                return True
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            return False
        return dfs(source)
# DFS Iterative
        if source == destination:
            return True
        #buiding a adjacency list, undirected graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # defining a seen set to detect duplicates and adding source to it
        seen = set()
        seen.add(source)
        # since iterative dfs, making use of stack and adding source to it
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        return False
# BFS using a queue
        if source == destination:
            return True
        q = deque()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        q.append(source)
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
        return False
