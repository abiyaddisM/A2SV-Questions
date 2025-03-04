# March 4 2025
# https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        flip = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                for k in range(max(0, i - 1), min(len(board), i + 2)):
                    for l in range(max(0, j - 1), min(len(board[i]), j + 2)):
                        if k == i and l == j:
                            continue
                        if board[k][l] == 1:
                            count += 1
                if (board[i][j] == 1 and (count < 2 or count > 3)) or (board[i][j] == 0 and count == 3):
                    flip.append([i,j])
        for f in flip:
            if board[f[0]][f[1]] == 1:
               board[f[0]][f[1]] = 0
            else:
                board[f[0]][f[1]] = 1 