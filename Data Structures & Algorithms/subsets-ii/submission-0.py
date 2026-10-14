class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        def solve(idx,temp):
            if idx == n:
                ans.append(temp[:])
                return
            
            #take
            temp.append(nums[idx])
            solve(idx + 1, temp)
            temp.pop()

            # not Take
            j = idx + 1
            while j < n and nums[j] == nums[idx]:
                j += 1
            
            solve(j,temp)
        
        solve(0,[])
        return ans
        