class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def solve(i,j):
            if i == 0 and j == 0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            left = solve(i,j-1)
            up = solve(i-1, j)

            dp[i][j] = up + left

            return dp[i][j]
        
        # return solve(m-1, n-1)
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                left = dp[i][j-1]
                up = dp[i-1][j]

                dp[i][j] = left + up
        
        return dp[m-1][n-1]