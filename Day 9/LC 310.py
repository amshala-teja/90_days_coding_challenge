# 310. Minimum Height Trees

# A tree is an undirected graph in which any two vertices are connected by exactly one path. 
# In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where 
# edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, 
# you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. 
# Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

# Example 1:


# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.


from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            result = []
            for i in range(n):
                result.append(i)
            return result
        

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        leaves = deque()
        for i in range(n):
            if len(g[i]) == 1:
                leaves.append(i)

        # Step 3: Trim leaves layer-by-layer
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = g[leaf].pop()  # only one neighbor
                g[neighbor].remove(leaf)
                if len(g[neighbor]) == 1:
                    leaves.append(neighbor)

        # Step 4: Remaining nodes are roots of MHTs
        return list(leaves)