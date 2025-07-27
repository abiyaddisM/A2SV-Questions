from collections import Counter,deque, defaultdict
import heapq
import math
import sys
def INT():
    return int(sys.stdin.readline())
def IA():
    return tuple(map(int, sys.stdin.readline().split()))
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

t = INT()
for _ in range(t):
    size, m1, m2 = IA()
    g1 = [IA() for _ in range(m1)]
    g2 = [IA() for _ in range(m2)]
    test = set()
    for g in g2:
        flip = (g[1], g[0])
        if g in test or flip in test:
            math.sqrt(-1)
        test.add(g)
    res = 0
    g2 = set(g2)
    for i in range(m1):
        flip = (g1[i][1], g1[i][0])
        if g1[i] not in g2 and flip not in g2:
            res += 1
            continue
        g2.remove(g1[i] if g1[i] in g2 else flip)
    res += len(g2)
    print(res)
