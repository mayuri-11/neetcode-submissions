class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        temp = []
        candidates.sort()

        def solve(idx,target):
            if target == 0:
                ans.append(temp[:])
                return
            
            if idx == n:
                return
            
            # take
            if candidates[idx] <= target:
                temp.append(candidates[idx])
                solve(idx + 1, target - candidates[idx])
                temp.pop()
            
            # notTake
            j = idx + 1
            while j < n and candidates[j] == candidates[idx]:
                j += 1
            
            solve(j,target)
        
        solve(0,target)
        return ans
        