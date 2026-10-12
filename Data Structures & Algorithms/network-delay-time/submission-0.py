class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]

        for u,v,w in times:
            graph[u].append([v,w])
        
        pq = []
        heapq.heappush(pq,(0,k))

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue
            
            for nei, wt in graph[node]:
                if d + wt < dist[nei]:
                    dist[nei] = d + wt
                    heapq.heappush(pq,(dist[nei],nei))
        
        time = 0
        for i in range(1,n + 1):
            if dist[i] == float('inf'):
                return -1
            
            time = max(time, dist[i])
        
        return time
            


        