# June 15 2025
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reach = set()
        res = []
        for e in edges:
            reach.add(e[1])
        for i in range(n):
            if i not in reach:
                res.append(i)
        return res
