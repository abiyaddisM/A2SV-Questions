# September 3 2025
# https://leetcode.com/problems/number-of-closed-islands/description/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        arr = [ [(i,j) for j in range(c)] for i in range(r)]
        def find(i, j):
            if arr[i][j] == (i, j):
                return (i, j)
            return find(arr[i][j][0], arr[i][j][1])

        def union(a, b):
            t1 = find(a[0], a[1])
            t2 = find(b[0], b[1])
            if t1 != t2:
                arr[t2[0]][t2[1]] = t1
        def inbound(i, j):
            return 0 <= i < r and 0 <= j < c
        dir = [ (0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    continue
                for dx, dy in dir:
                    cx = i + dx
                    cy = j + dy
                    if inbound(cx, cy) and grid[cx][cy] == 0:
                        union( (i,j), (cx, cy))
        dic = {}
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    continue
                root = find(i, j)
                state = True
                for dx, dy in dir:
                    cx = i + dx
                    cy = j + dy
                    if not inbound(cx, cy):
                        state = False
                if root in dic:
                    if dic[root]:
                        dic[root] = state
                else:
                    dic[root] = state
        res = 0
        for k, v in dic.items():
            if v:
                res += 1
        return res
