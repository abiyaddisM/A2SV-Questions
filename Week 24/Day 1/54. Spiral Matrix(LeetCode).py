# July 7 2025
# https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        visited = [ [False for _ in range(col)] for _ in range(row)]
        res = []
        def helper(i, j, ac):
            visited[i][j] = True
            res.append(mat[i][j])
            cx, cy = ac[0] + i, ac[1] + j
            if inbound(cx,cy) and not visited[cx][cy]:
                helper(cx, cy, ac)
            else:
                for dx, dy in dir:
                    cx, cy = dx + i, dy + j
                    if inbound(cx,cy) and not visited[cx][cy]:
                        helper(cx, cy, [dx, dy])
                        break

        helper(0, 0, [0, 1])
        return res