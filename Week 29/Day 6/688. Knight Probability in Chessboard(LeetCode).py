# August 16 2025
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(2, 1), (-2, 1), (2, -1), (-2, -1),
                (1, 2), (-1, 2), (1, -2), (-1, -2)]

        prev = [[1.0 for _ in range(n)] for _ in range(n)]

        for _ in range(1, k + 1):
            curr = [[0.0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    prob = 0.0
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            prob += prev[nr][nc] / 8.0
                    curr[r][c] = prob
            prev = curr

        return prev[row][column]
