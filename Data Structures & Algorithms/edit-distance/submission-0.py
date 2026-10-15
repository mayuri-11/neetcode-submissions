class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1] * m for _ in range(n)]
        def solve(i,j):

            if i < 0:
                return j + 1
            
            if j < 0:
                return i + 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                return 0 + solve(i-1,j-1)
            
            insert = 1 + solve(i,j-1)
            delete = 1 + solve(i-1,j)
            replace = 1 + solve(i-1,j-1)

            dp[i][j] = min(insert,delete,replace)
            return dp[i][j]
        
        return solve(n-1,m-1)
        