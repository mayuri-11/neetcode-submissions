class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]
        for i in range(1,n):
            temp = maxi
            maxi = max(nums[i], nums[i] * maxi, nums[i] * mini)
            mini = min(nums[i], temp * nums[i], nums[i] * mini)

            ans = max(ans,maxi)
        
        return ans
        
        