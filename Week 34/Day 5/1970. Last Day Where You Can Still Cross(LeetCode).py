# September 19 2025
# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        nums = [[0 for j in range(col)] for i in range(row)]
        parent = [[(i, j) for j in range(col)] for i in range(row)]
        rank = [[0 for j in range(col)] for i in range(row)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        dic = defaultdict(set)

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        def find(i, j):
            pi, pj = parent[i][j]
            if (pi, pj) != (i, j):
                parent[i][j] = find(pi, pj)
            return parent[i][j]

        def union(a, b):
            ai, aj = find(a[0], a[1])
            bi, bj = find(b[0], b[1])
            if (ai, aj) == (bi, bj):
                return
            r1 = rank[ai][aj]
            r2 = rank[bi][bj]
            if r1 < r2:
                parent[ai][aj] = (bi, bj)
                dic[(bi, bj)] = dic[(bi, bj)] | dic[(ai, aj)]
                dic.pop((ai, aj))
            elif r1 > r2:
                parent[bi][bj] = (ai, aj)
                dic[(ai, aj)] = dic[(bi, bj)] | dic[(ai, aj)]
                dic.pop((bi, bj))
            else:
                parent[bi][bj] = (ai, aj)
                dic[(ai, aj)] = dic[(bi, bj)] | dic[(ai, aj)]
                dic.pop((bi, bj))
                rank[ai][aj] += 1

        res = 0
        for c in cells:
            i, j = c
            i -= 1
            j -= 1
            nums[i][j] = 1
            for dx, dy in dir:
                cx = dx + i
                cy = dy + j
                if inbound(cx, cy) and nums[cx][cy] == 1:
                    union((cx, cy), (i, j))
            p = find(i, j)
            dic[p].add(j)
            print(dic[p], col)
            if len(dic[p]) == col:
                return res
            res += 1