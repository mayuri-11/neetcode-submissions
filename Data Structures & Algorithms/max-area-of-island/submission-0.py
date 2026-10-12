class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxi = 0
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def solve(i, j, area):
            visited.add((i, j))

            for dr, dc in directions:
                nr = i + dr
                nc = j + dc

                if (0 <= nr < row and 0 <= nc < col and
                    grid[nr][nc] == 1 and (nr, nc) not in visited):

                    self.area += 1
                    solve(nr, nc, self.area)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.area = 1
                    solve(i, j, self.area)
                    maxi = max(maxi, self.area)

        return maxi