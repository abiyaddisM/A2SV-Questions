# July 4 2025
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        res = [-1] * n
        visited = [[False, False] for _ in range(n)]
        que = deque([(0, 0), (0, 1)])
        level = 0

        while que:
            for _ in range(len(que)):
                node, color = que.popleft()
                if res[node] == -1:
                    res[node] = level

                if color == 0:
                    for nei in blue_graph[node]:
                        if not visited[nei][1]:
                            visited[nei][1] = True
                            que.append((nei, 1))
                else:
                    for nei in red_graph[node]:
                        if not visited[nei][0]:
                            visited[nei][0] = True
                            que.append((nei, 0))
            level += 1

        return res
