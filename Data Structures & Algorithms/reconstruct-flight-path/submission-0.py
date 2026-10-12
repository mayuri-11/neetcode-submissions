from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        for node in graph:
            graph[node].sort(reverse=True)

        path = []

        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)

            path.append(node)

        dfs("JFK")

        return path[::-1]