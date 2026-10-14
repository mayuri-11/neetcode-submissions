class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def solve(idx, summ):
            if idx == n:
                if summ == target:
                    return 1
                return 0

            if (idx, summ) in dp:
                return dp[(idx, summ)]

            plus = solve(idx + 1, summ + nums[idx])
            minus = solve(idx + 1, summ - nums[idx])

            dp[(idx, summ)] = plus + minus
            return dp[(idx, summ)]

        return solve(0, 0)
        