class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        n = len(points)

        for i in range(n):
            point = points[i]
            dis = point[0] * point[0] + point[1] * point[1]

            heapq.heappush(pq,(-dis,point))

            if len(pq) > k:
                heapq.heappop(pq)
        
        ans = []
        while pq:
            d,temp =  heapq.heappop(pq)
            ans.append(temp)
        
        return ans
        