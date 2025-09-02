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


q = INT()
out_lines = []
for _ in range(q):
    n = INT()
    p = IA()
    p = [x-1 for x in p]
    ans = [0]*n
    visited = [False]*n

    for i in range(n):
        if ans[i] != 0:
            continue
        cycle = []
        j = i
        while not visited[j]:
            visited[j] = True
            cycle.append(j)
            j = p[j]
        L = len(cycle)
        for v in cycle:
            ans[v] = L

    print(' '.join(map(str, ans)))
