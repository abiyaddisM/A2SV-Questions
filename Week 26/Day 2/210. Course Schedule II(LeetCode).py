# July 22 2025
# https://leetcode.com/problems/course-schedule-ii/description/
class Solution:
    def findOrder(self, nc: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(nc)]
        degree = [0 for _ in range(nc)]
        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1
        que = deque()
        for i in range(nc):
            if degree[i] == 0:
                que.append(i)
        res = []
        while que:
            node = que.popleft()
            res.append(node)
            for i in graph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)
            node = []
        if len(res) != nc:
            return []
        return res