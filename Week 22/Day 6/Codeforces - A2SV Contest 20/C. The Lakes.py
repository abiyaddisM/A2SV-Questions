from collections import Counter,deque
import math
import sys

def INT():
    return int(sys.stdin.readline())

def IA():
    return list(map(int, sys.stdin.readline().split()))


t = INT()
for _ in range(t):
    n, m = IA()
    graph = []
    for i in range(n):
        graph.append(IA())
    visited = [ [False for __ in range(m)] for ___ in range(n)]
    dir = [ (1, 0), (-1, 0), (0, 1), (0, -1)]
    def helper(row, col):
        total = 0
        stack = [(row, col)]
        while stack:
            i, j = stack.pop()
            if not (0 <= i < n and 0 <= j < m):
                continue
            if visited[i][j] or graph[i][j] == 0:
                continue
            visited[i][j] = True
            total += graph[i][j]
            for dx, dy in dir:
                cx = i + dx
                cy = j + dy
                stack.append((cx, cy))
        return total
    res = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                res = max(res, helper(i, j))
    print(res)

