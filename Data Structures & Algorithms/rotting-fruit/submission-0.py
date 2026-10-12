class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        fresh = 0
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    q.append((i,j))
        
        if fresh == 0:
            return 0
        
        time = 0

        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while q and fresh > 0:
            size = len(q)
            for temp in range(size):
                i,j = q.popleft()

                for dr,dc in direction:
                    nr = dr + i
                    nc = dc + j

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            
            time += 1
        
        if fresh > 0:
            return -1
        
        return time

                
        

        