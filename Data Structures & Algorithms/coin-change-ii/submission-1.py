class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def solve(idx, target):
            if target == 0:
                return 1
            
            if idx == 0:
                if target % coins[0] == 0:
                    return 1
                return 0
            
            if idx < 0:
                return 0
            
            if dp[idx][target] != -1:
                return dp[idx][target]
            
            take = 0
            if coins[idx] <= target:
                take = solve(idx, target - coins[idx])
            
            notTake = solve(idx - 1, target)

            dp[idx][target] = take + notTake
            return dp[idx][target]
        
        return solve(n-1,amount)

        