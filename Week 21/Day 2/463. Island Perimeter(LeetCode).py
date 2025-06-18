# June 17 2025
# https://leetcode.com/problems/island-perimeter/description/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def helper(grid, visited, row, col):
            if visited[row][col]:
                return
            visited[row][col] = True

            for rc, cc in dir:
                nr = row + rc
                nc = col + cc
                if not inbound(nr, nc) or grid[nr][nc] == 0:
                    self.res += 1
                elif not visited[nr][nc]:
                    helper(grid, visited, nr, nc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    helper(grid, visited, i, j)
                    break
        return self.res