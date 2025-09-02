# September 2 2025
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        arr = [i for i in range(n)]
        opt = [0 for i in range(n)]
        def find(x):
            if arr[x] == x:
                return x
            temp = find(arr[x])
            arr[x] = temp
            return temp
        def union(a,b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                if opt[t1] == opt[t2]:
                    arr[t2] = t1
                    opt[t2] += 1
                elif opt[t1] > opt[t2]:
                    arr[t1] = t2
                else:
                    arr[t2] = t1

        for r in roads:
            union(r[0] - 1, r[1] - 1)
        res =  float('inf')
        temp = find(arr[-1])
        for r in roads:
            t = find(arr[r[0] - 1])
            if  t == temp:
                res = min(res, r[-1])
        return res