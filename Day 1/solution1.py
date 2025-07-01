# LC 2385. Amount of Time for Binary Tree to Be Infected

# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        graph  = defaultdict(list)
        def new_graph(node, parent):
            if not node:
                return 
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            new_graph(node.left, node)
            new_graph(node.right, node)
        new_graph(root, None)
        # now apply bfs to spread the infection
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)

        time = -1 #since the first pop happens at 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            time += 1
        return time







        