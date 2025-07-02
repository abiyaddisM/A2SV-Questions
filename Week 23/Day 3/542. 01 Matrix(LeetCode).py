# July 2 2025
# https://leetcode.com/problems/01-matrix/description/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        res = [[-1 for _ in range(col)] for __ in range(row)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for dx, dy in dir:
                cx, cy = dx + i, dy + j
                if inbound(cx, cy) and res[cx][cy] == -1:
                    res[cx][cy] = res[i][j] + 1
                    queue.append((cx, cy))
        return res