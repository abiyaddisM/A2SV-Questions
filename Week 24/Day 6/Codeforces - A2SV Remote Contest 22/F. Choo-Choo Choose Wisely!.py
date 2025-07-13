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
full = [[] for _ in range(n + 1)]
road = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = IA()
    full[u].append((v,w))
    full[v].append((u, w))
    road[u].append((v,w))
    road[v].append((u, w))

train = []
for i in range(k):
    s, y = IA()
    train.append((s, y))
    full[1].append((s, y))
    full[s].append((1, y))
dist = [float('inf')] * (n + 1)
dist[1] = 0
qp = [(0, 1)]
while qp:
    d, u = heapq.heappop(qp)
    if d > dist[u]:
        continue
    for v, w in full[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(qp, (dist[v], v))
cc = 0
tos = {}
for s, y in train:
    if dist[s] < y:
        cc += 1
    elif dist[s] == y:
        if s not in tos:
            tos[s] = 0
        tos[s] += 1
for s, count in tos.items():
    pv = False
    for v, w in road[s]:
        if dist[v] + w == dist[s]:
            pv = True
            break
    if pv:
        cc += count
    else:
        cc += count - 1
print(cc)
