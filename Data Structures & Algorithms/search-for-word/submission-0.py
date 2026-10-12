class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(word)
        
        def solve(i,j,idx):

            if idx == n:
                return True
            
            temp = board[i][j]
            board[i][j] = "#"

            for dr, dc in directions:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == word[idx]:
                    if solve(nr,nc,idx + 1):
                        board[i][j] = temp
                        return True
            
            board[i][j] = temp
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if solve(i,j,1):
                        return True
        
        return False

        