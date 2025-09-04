# September 4 2025
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/
from typing import List
from collections import defaultdict


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = [i for i in range(len(source))]

        def find(x):
            if x == parent[x]:
                return x
            temp = find(parent[x])
            parent[x] = temp
            return temp

        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                parent[t2] = t1

        for a in allowedSwaps:
            union(a[0], a[1])

        sourceDic = defaultdict(lambda: defaultdict(int))
        targetDic = defaultdict(lambda: defaultdict(int))

        for i in range(len(parent)):
            root = find(parent[i])
            sourceDic[root][source[i]] += 1
            targetDic[root][target[i]] += 1

        res = 0
        for k, sv in sourceDic.items():
            tv = targetDic[k]
            compSize = sum(sv.values())
            matches = 0
            for k1, v1 in sv.items():
                matches += min(v1, tv.get(k1, 0))
            res += compSize - matches

        return res
