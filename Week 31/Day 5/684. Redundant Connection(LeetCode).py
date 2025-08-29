# August 29 2025
# https://leetcode.com/problems/redundant-connection/description/
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []

