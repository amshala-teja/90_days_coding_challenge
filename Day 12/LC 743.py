# 743. Network Delay Time

# You are given a network of n nodes, labeled from 1 to n. You are also given times, 
# a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. 
# Return the minimum time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = defaultdict(list)
        for u, v, time in times:
            g[u].append((v, time))
        min_times = {}
        min_heap = [(0, k)] #dist from source to node
        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            min_times[i] = time_k_to_i
            for nei, nei_time in g[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1