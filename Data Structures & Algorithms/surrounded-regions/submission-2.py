
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        q = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row - 1 or j == col - 1) and board[i][j] == "O":
                    q.append((i, j))
                    board[i][j] = "#"

        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                nr = i + dr
                nc = j + dc

                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
