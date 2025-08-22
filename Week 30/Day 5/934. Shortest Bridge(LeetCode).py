# August 22 2025
# https://leetcode.com/problems/shortest-bridge/description/
from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n

        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            for dx, dy in dirs:
                dfs(i + dx, j + dy)

        found = False
        for i in range(n):
            if found: break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if inbound(x, y) and grid[x][y] == 0:
                            grid[x][y] = 3
                            q.append((x, y, 1))

        while q:
            i, j, d = q.popleft()
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if not inbound(x, y):
                    continue
                if grid[x][y] == 1:
                    return d
                if grid[x][y] == 0:
                    grid[x][y] = 3
                    q.append((x, y, d + 1))

        return -1
