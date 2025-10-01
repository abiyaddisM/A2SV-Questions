# October 1 2025
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [ [float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        for f,t,w in edges:
            graph[f][t] = w
            graph[t][f] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[j][k]:
                        graph[i][j] = graph[i][k] + graph[j][k]
        temp = []
        for i in range(n):
            count = 0
            for j in range(n):
                if graph[i][j] == 0:
                    continue
                if graph[i][j] <= distanceThreshold:
                    count += 1
            temp.append(count)
        res = (0 ,temp[0])
        for i in range(1, n):
            if temp[i] <= res[1]:
                res = (i, temp[i])
        return res[0]