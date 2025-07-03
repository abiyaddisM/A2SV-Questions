# July 3 2025
# https://leetcode.com/problems/rotting-oranges/description/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        que = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    que.append([i, j])
        level = 0
        while que:
            size = len(que)
            for i in range(size):
                i, j = que.popleft()
                for dx, dy in dir:
                    cx, cy = dx + i, dy + j
                    if inbound(cx, cy) and grid[cx][cy] == 1:
                        grid[cx][cy] = 2
                        que.append([cx, cy])
            level += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return level - 1 if level != 0 else 0