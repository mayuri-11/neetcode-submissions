class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def solve(idx):
            if idx == n:
                return 1
            
            if s[idx] == "0":
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            one = solve(idx + 1)
            two = 0

            if idx + 1 < n and 10 <= int(s[idx:idx+2]) <= 26:
                two = solve(idx + 2)
            
            dp[idx] = one + two
            return dp[idx]
        
        return solve(0)
        