# July 23 2025
# https://leetcode.com/problems/course-schedule-iv/description/
class Solution:
    def checkIfPrerequisite(self, nc: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(nc)]
        degree = [0 for _ in range(nc)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
            degree[p[1]] += 1

        pre = [set() for _ in range(nc)]
        que = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                que.append(i)
        while que:
            node = que.popleft()
            for i in graph[node]:
                pre[i].update(pre[node])
                pre[i].add(node)
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)
            graph[node] = []
        res = []
        for q in queries:
            res.append(q[0] in pre[q[1]])
        return res

