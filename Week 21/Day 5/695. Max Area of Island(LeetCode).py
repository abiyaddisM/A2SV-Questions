# June 20 2025
# https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.count = 1
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def helper(row, col):
            visited[row][col] = True
            self.res = max(self.res, self.count)
            for row_count, col_count in dir:
                new_row = row + row_count
                new_col = col + col_count
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    self.count += 1
                    helper(new_row, new_col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.count = 1
                    helper(i, j)
        return self.res