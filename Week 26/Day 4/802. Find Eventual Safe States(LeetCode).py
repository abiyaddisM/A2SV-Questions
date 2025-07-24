# July 24 2025
# https://leetcode.com/problems/find-eventual-safe-states/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nGraph = [[] for _ in range(len(graph))]
        degree = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            for g in graph[i]:
                nGraph[g].append(i)
                degree[i] += 1
        que = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
        res = []
        while que:
            node = que.popleft()
            res.append(node)
            for i in nGraph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)
        res.sort()
        return res