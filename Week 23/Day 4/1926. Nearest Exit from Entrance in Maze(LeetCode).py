# July 3 2025
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        visited = [[False for _ in range(col)] for __ in range(row)]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        que = deque([entrance])
        visited[entrance[0]][entrance[1]] = True
        level = 0
        while que:
            size = len(que)
            for i in range(size):
                i, j = que.popleft()
                for dx, dy in dir:
                    cx, cy = dx + i, dy + j
                    if inbound(cx, cy) and not visited[cx][cy] and maze[cx][cy] == '.':
                        if cx == row - 1 or cy == col - 1 or cx == 0 or cy == 0:
                            return level + 1
                        que.append([cx, cy])
                        visited[cx][cy] = True

            level += 1

        return -1