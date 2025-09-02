# September 1 2025
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        arr = [i for i in range(len(stones))]

        def find(x):
            if x == arr[x]:
                return x

            return find(arr[x])

        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                arr[t2] = t1

        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        components = {find(i) for i in range(len(stones))}
        return len(stones) - len(components)