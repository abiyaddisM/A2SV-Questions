# June 17 2025
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        def helper(node, visited):
            if node in visited:
                return False
            if node == destination:
                return True
            visited.add(node)
            for n in graph[node]:
                if helper(n, visited):
                    return True
            return False
        return helper(source, set())
