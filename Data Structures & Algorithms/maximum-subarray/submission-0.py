class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0
            
            curr += num
            maxi = max(maxi,curr)
        
        return maxi
        