import sys, threading
from collections import Counter,deque, defaultdict
import heapq
import math
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

size, k = IA()
cats = IA()
graph = [[] for _ in range(size)]
for _ in range(size - 1):
    u, v = IA()
    u -=1
    v -=1
    graph[u].append(v)
    graph[v].append(u)
res = 0
que = deque([[0, cats[0], -1]])

while que:
    curInd, cat, p = que.popleft()
    if cat > k:
        continue
    leaf = (curInd != 0 and len(graph[curInd])  == 1) or (curInd == 0 and len(graph[curInd]) == 0)
    if leaf:
        res += 1
        continue
    for nextInd in graph[curInd]:
        if nextInd == p:
            continue
        newCat = cat + 1 if cats[nextInd] == 1 else 0

        que.append([nextInd, newCat, curInd])
print(res)
