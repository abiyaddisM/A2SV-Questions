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



size, m = IA()
graph = [ [] for _ in range(size)]
for _ in range(m):
    i, j, w = IA()
    i -= 1
    j -= 1
    graph[i].append([j, w])
    graph[j].append([i, w])
distance = [ float('inf') for _ in range(size)]
p = [-1] * size
distance[0] = 0
heap = [(0, 0)]
while heap:
    curDis, curInd = heapq.heappop(heap)
    if curDis > distance[curInd]:
        continue
    for nextInd, nextDis  in graph[curInd]:
        newDis = nextDis + curDis
        if newDis < distance[nextInd]:
            distance[nextInd] = newDis
            p[nextInd] = curInd
            heapq.heappush(heap, (newDis, nextInd))

if distance[-1] == float('inf'):
    print(-1)
else:
    res = []
    temp = size - 1
    while temp != -1:
        res.append(temp)
        temp = p[temp]
    res.reverse()
    PA(n + 1 for n in res)