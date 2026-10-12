class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        n = len(stones)

        for i in range(n):
            heapq.heappush(pq,-stones[i])
        
        while len(pq) > 1:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)

            if x > y or y > x:
                heapq.heappush(pq,-abs(x-y))
        
        if pq:
            return -heapq.heappop(pq)
        else:
            return 0
        