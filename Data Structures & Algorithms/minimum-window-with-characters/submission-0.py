class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapp = {}
        for c in t:
            mapp[c] = mapp.get(c,0) + 1
        
        left = 0
        count = len(t)
        ans = ""
        mini = float('inf')

        for right in range(len(s)):
            rightChar = s[right]

            if rightChar in mapp:
                if mapp[rightChar] > 0:
                    count -= 1
                mapp[rightChar] -= 1
            
            while count == 0:
                if right - left + 1 < mini:
                    ans = s[left:right + 1]
                    mini = right - left + 1
                
                leftChar = s[left]

                if leftChar in mapp:
                    mapp[leftChar] += 1
                    if mapp[leftChar] > 0:
                        count += 1
                
                left += 1
            
        return ans





        