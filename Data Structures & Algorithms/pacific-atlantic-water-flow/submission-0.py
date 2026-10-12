class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        p = [[False] * col for _ in range(row)]
        a = [[False] * col for _ in range(row)]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def solve(i,j,visited):
            visited[i][j] = True

            for dr, dc in directions:
                nr = dr + i
                nc = dc + j

                if 0 <= nr < row and 0 <= nc < col and heights[nr][nc] >= heights[i][j] and not visited[nr][nc]:
                    solve(nr,nc,visited)
        
        for i in range(row):
            if not p[i][0]:
                solve(i,0,p)
        
        for j in range(col):
            if not p[0][j]:
                solve(0,j,p)
        
        for i in range(row):
            if not a[i][col - 1]:
                solve(i,col - 1,a)
        
        for j in range(col):
            if not a[row - 1][j]:
                solve(row - 1,j,a)
        
        ans = []
        for i in range(row):
            for j in range(col):
                if p[i][j] and a[i][j]:
                    ans.append([i,j])
        
        return ans
        


        