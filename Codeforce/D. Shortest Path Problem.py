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

n, m = IA()
graph = [ [] for _ in range(n)]
for _ in range(m):
    u, v, w = IA()
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
visited = set()

