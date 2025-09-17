# September 17 2025
# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        dir = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)]
        for i in range(n - 2):
            temp = []
            for j in range(n - 2):
                m = grid[i][j]
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    m = max(m, grid[x][y])
                temp.append(m)
            res.append(temp)
        return res