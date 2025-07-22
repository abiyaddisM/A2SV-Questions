# July 22 2025
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            degree[b] += 1
        que = deque()
        for i in range(n):
            if degree[i] == 0:
                que.append(i)
        temp = [set() for _ in range(n)]
        while que:
            node = que.popleft()
            for i in graph[node]:
                degree[i] -= 1
                temp[i].update(temp[node])
                temp[i].add(node)
                if degree[i] == 0:
                    que.append(i)
            graph[node] = []
        res = []
        for t in temp:
            tt = list(t)
            tt.sort()
            res.append(tt)
        return res