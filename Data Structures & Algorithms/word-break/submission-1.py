class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n
        seen = set(wordDict)
        
        def solve(idx):
            if idx == n:
                return True
            
            if dp[idx] != -1:
                return dp[idx]
            
            for i in range(idx,n):
                word = s[idx:i+1]
                if word in seen:
                    if solve(i+1):
                        dp[idx] = True
                        return True
            
            dp[idx] = False
            return False
        
        return solve(0)
        