# June 20 2025
# https://leetcode.com/problems/surrounded-regions/description/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [ [False for _ in range(len(board[0]))] for __ in range(len(board))]
        dir = [ (1, 0), (-1, 0), (0, 1), (0, -1)]
        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))

        def helper(row, col):
            if board[row][col] != 'O':
                return
            visited[row][col] = True
            board[row][col] = 'S'
            for i, j in dir:
                nr = row + i
                nc = col + j
                if inbound(nr, nc) and board[nr][nc] == 'O' and not visited[nr][nc]:
                    helper(nr, nc)

        for i in range(len(board)):
            helper(i, 0)
            helper(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            helper(0, j)
            helper(len(board) - 1,  j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
