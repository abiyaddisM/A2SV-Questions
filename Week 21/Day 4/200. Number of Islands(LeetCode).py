# June 19 2025
# https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        res = 0
        def helper(row, col):
            visited[row][col] = True
            for rc, cc in dir:
                nr = row + rc
                nc = col + cc
                if inbound(nr, nc) and grid[nr][nc] == '1' and not visited[nr][nc]:
                    helper(nr, nc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    helper(i, j)
        return res


