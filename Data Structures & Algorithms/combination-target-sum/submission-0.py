class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        temp = []

        def solve(idx,target):
            if target == 0:
                ans.append(temp[:])
                return
            
            if idx == n:
                return
            
            # take
            if nums[idx] <= target:
                temp.append(nums[idx])
                solve(idx,target - nums[idx])
                temp.pop()

            # not take
            solve(idx + 1,target)
        
        solve(0,target)

        return ans

        