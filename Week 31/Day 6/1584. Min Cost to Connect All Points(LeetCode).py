# August 30 2025
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = [i for i in range(len(points))]

        def find(x):
            if x == arr[x]:
                return x

            return find(arr[x])

        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                arr[t2] = t1

        temp = []
        for i in range(len(points) - 1):
            for j in range(len(points)):
                Xi, Yi = points[i]
                Xj, Yj = points[j]
                t = abs(Xi - Xj) + abs(Yi - Yj)
                temp.append((t, i, j))
        temp.sort()
        res = 0
        for t in temp:
            val, i, j = t
            t1 = find(i)
            t2 = find(j)
            if t1 != t2:
                union(i, j)
                res += val

        return res