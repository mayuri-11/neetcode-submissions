class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def solve(idx,temp):
            if idx == n:
                ans.append(temp[:])
                return
            
            # take
            temp.append(nums[idx])
            solve(idx + 1,temp)
            temp.pop()

            # not take
            solve(idx + 1,temp)
        
        solve(0,[])

        return ans

        