# June 24 2025
# https://leetcode.com/problems/n-queens-ii/description/
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        grid = [[0 for _ in range(n)] for __ in range(n)]

        def check(grid, row, col):
            x, y = row, col
            while x > 0 and y > 0:
                x -= 1
                y -= 1
            while x < n and y < n:
                if grid[x][y] == 1:
                    return False
                x += 1
                y += 1

            x, y = row, col
            while x > 0 and y < n - 1:
                x -= 1
                y += 1
            while x < n and y > 0:
                if grid[x][y] == 1:
                    return False
                x += 1
                y -= 1

            for i in range(n):
                if grid[i][col] == 1 or grid[row][i] == 1:
                    return False
            return True

        def helper(grid, row, col):
            if row == n:
                self.res += 1
                return
            for j in range(n):
                if check(grid, row, j):
                    grid[row][j] = 1
                    helper(grid, row + 1, 0)
                    grid[row][j] = 0
            return

        for j in range(n):
            grid[0][j] = 1
            helper(grid, 1, 0)
            grid[0][j] = 0

        return self.res