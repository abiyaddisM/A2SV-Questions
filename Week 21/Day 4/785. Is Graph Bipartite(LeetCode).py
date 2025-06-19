# June 19 2025
# https://leetcode.com/problems/is-graph-bipartite/description/
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        def helper(current, count):
            color[current] = count % 2
            for neighbor in graph[current]:
                if color[neighbor] == -1:
                    if not helper(neighbor, count + 1):
                        return False
                elif color[neighbor] == color[current]:
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not helper(i, 0):
                    return False
        return True
