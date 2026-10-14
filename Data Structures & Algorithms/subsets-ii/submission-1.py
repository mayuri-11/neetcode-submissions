class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        temp = []

        def solve(idx):
            if idx == n:
                ans.append(temp[:])
                return
            
            #take
            temp.append(nums[idx])
            solve(idx + 1)
            temp.pop()

            # not Take
            j = idx + 1
            while j < n and nums[j] == nums[idx]:
                j += 1
            
            solve(j)
        
        solve(0)
        return ans
        