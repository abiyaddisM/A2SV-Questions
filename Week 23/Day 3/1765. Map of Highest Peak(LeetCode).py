# July 2 2025
# https://leetcode.com/problems/map-of-highest-peak/description/
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water = []
        row, col = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(col)] for __ in range(row)]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return (0 <= r < row and 0 <= c < col)

        queue = deque()

        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    queue.append((i, j))
        while queue:
            r, c = queue.popleft()
            for dx, dy in dir:
                rx = dx + r
                ry = dy + c
                if inbound(rx, ry) and res[rx][ry] == -1:
                    res[rx][ry] = res[r][c] + 1
                    queue.append((rx, ry))

        return res