# October 6 2025
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [ [float('inf') for _ in range(26)] for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for k in range(len(original)):
            i = ord(original[k]) - 97
            j = ord(changed[k]) - 97
            if graph[i][j] > cost[k]:
                graph[i][j] = cost[k]
        for k in range(26):
            for i in range(26):
                if graph[i][k] == float('inf'):
                        continue
                for j in range(26):
                    if graph[k][j] == float('inf'):
                        continue
                    if graph[i][k] + graph[k][j] < graph [i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        res = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            d = graph[ord(s) - 97][ord(t) - 97]
            if d == float('inf'):
                return -1
            res += d
        return res 