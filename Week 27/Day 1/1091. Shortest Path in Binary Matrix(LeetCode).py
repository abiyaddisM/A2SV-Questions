# July 28 2025
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (-1, 1), (1, -1), (-1, -1)]

        queue = deque([(0, 0, 1)])
        visited = set((0, 0))

        while queue:
            x, y, dist = queue.popleft()
            if x == n - 1 and y == n - 1:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < n
                    and grid[nx][ny] == 0
                    and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return -1
