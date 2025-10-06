import sys
from collections import deque

def IA():
    return list(map(int, sys.stdin.readline().split()))

def bfs(graph, n):
    q = deque([0])
    visited = [False]*n
    visited[0] = True
    dist = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            if u == n-1:
                return dist
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        dist += 1
    return -1

n, m = IA()
rail = [set() for _ in range(n)]
for _ in range(m):
    u, v = IA()
    u -= 1; v -= 1
    rail[u].add(v)
    rail[v].add(u)

road = [set() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and j not in rail[i]:
            road[i].add(j)

if (n-1) in rail[0]:
    ans = bfs(road, n)
else:
    ans = bfs(rail, n)

print(ans)
