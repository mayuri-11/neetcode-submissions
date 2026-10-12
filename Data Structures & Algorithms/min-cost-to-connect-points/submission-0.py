class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1,n):
                x = points[i]
                y = points[j]

                d = abs(x[0] - y[0]) + abs(x[1] - y[1])

                graph[i].append([j,d])
                graph[j].append([i,d])
        
        visited = set()
        pq = []
        heapq.heappush(pq,(0,0,-1))

        mst = []
        summ = 0

        while pq:
            wt,node,parent = heapq.heappop(pq)

            if node in visited:
                continue
            
            visited.add(node)
            summ += wt

            if parent != -1:
                mst.append((parent,node))
            
            for nei, neiWt in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq,(neiWt,nei,node))
        
        return summ
        

        