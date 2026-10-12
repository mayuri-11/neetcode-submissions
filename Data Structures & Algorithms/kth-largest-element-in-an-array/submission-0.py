class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(hq,nums[i])

            if len(hq) > k:
                heapq.heappop(hq)
            
        return heapq.heappop(hq)

        