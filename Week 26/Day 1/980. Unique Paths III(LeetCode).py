# July 21 2025
# https://leetcode.com/problems/unique-paths-iii/description/
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        visited = [[0 for _ in range(m)] for _ in range(n)]
        space = 0
        start = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    space += 1
                elif grid[i][j] == 1:
                    start = [i, j]
        self.res = 0

        def helper(i, j, count):
            visited[i][j] = 1
            for dx, dy in dir:
                cx, cy = dx + i, dy + j
                if inbound(cx, cy) and not visited[cx][cy] and grid[cx][cy] != -1:
                    helper(cx, cy, count + 1)
            visited[i][j] = 0
            if count == space and grid[i][j] == 2:
                self.res += 1

        helper(start[0], start[1], -1)
        return self.res

