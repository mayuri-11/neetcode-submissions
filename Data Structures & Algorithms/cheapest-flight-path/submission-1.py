
from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append([v, w])

        q = deque()
        q.append((0, src, 0))  # cost, node, stops

        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            d, node, stops = q.popleft()

            if stops > k:
                continue

            for nei, wt in graph[node]:
                new_cost = d + wt

                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((new_cost, nei, stops + 1))

        return -1 if dist[dst] == float('inf') else dist[dst]
