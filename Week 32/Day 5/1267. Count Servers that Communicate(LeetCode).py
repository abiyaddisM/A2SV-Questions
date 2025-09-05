# September 5 2025
# https://leetcode.com/problems/count-servers-that-communicate/description/
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        parent = [[(i, j) for j in range(c)] for i in range(r)]
        rank = [[0 for j in range(c)] for i in range(r)]

        def find(x):
            if parent[x[0]][x[1]] == x:
                return x
            temp = find(parent[x[0]][x[1]])
            parent[x[0]][x[1]] = temp
            return temp

        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                r1 = rank[t1[0]][t1[1]]
                r2 = rank[t2[0]][t2[1]]
                if r1 == r2:
                    parent[t1[0]][t1[1]] = t2
                    rank[t2[0]][t2[1]] += 1
                elif r1 < r2:
                    parent[t1[0]][t1[1]] = t2
                else:
                    parent[t2[0]][t2[1]] = t1

        rowDic = {}
        colDic = {}
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 1:
                    continue
                if i in rowDic:
                    union((i, j), rowDic[i])
                if j in colDic:
                    union((i, j), colDic[j])
                rowDic[i] = (i, j)
                colDic[j] = (i, j)
        dic = defaultdict(int)
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 1:
                    continue
                p = find(parent[i][j])
                dic[p] += 1
        res = 0
        for k, v in dic.items():
            if v > 1:
                res += v
        return res



