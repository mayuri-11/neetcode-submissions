class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        maxArea = 0

        for i in range(n+1):
            if i == n:
                h = 0
            else:
                h = heights[i]
            
            while st and h < heights[st[-1]]:
                hei = heights[st.pop()]

                if not st:
                    w = i
                else:
                    w = i - st[-1] - 1
                
                area = hei * w
                maxArea = max(area, maxArea)
            
            st.append(i)
        
        return maxArea
            

        