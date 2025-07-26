# July 26 2025
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        visited = set()
        def helper(node, path):
            path.append(node)
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    helper(i, path)
            if node == n - 1:
                res.append(path[:])
            path.pop()
            visited.remove(node)

        helper(0, [])
        return res