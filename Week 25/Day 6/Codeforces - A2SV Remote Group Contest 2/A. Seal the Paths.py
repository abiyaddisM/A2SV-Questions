from collections import Counter,deque, defaultdict
import heapq
import math
import sys
def INT():
    return int(sys.stdin.readline())
def IA():
    return list(map(int, sys.stdin.readline().split()))
def SA():
    return input().split()
def STR():
    return sys.stdin.readline()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')

n, m, k = IA()

mat = []
for _ in range(n):
    temp = list(STR())
    temp.pop()
    mat.append(temp)
start = [0, 0]
for i in range(n):
    for j in range(m):
        if mat[i][j] == '.':
            start = [i, j]
            break
visited = [[False for _ in range(m)] for _ in range(n)]
dir = [ (0, 1), (1, 0), (-1, 0), (0, -1)]
def inbound(i, j):
    return 0 <= i < n and 0 <= j < m

count = 0
def dfs(start_i, start_j):
    global count, visited, mat
    stack = [(start_i, start_j, False)]

    while stack:
        i, j, post = stack.pop()

        if post:
            if count < k:
                mat[i][j] = 'X'
            count += 1
            continue

        if visited[i][j]:
            continue

        visited[i][j] = True
        stack.append((i, j, True))  # Mark for post-processing

        for dx, dy in dir:
            cx, cy = i + dx, j + dy
            if inbound(cx, cy) and not visited[cx][cy] and mat[cx][cy] != '#' and mat[cx][cy] != 'X':
                stack.append((cx, cy, False))

dfs(start[0], start[1])
for m in mat:
    print(''.join(m) )