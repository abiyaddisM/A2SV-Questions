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



t = INT()
for _ in range(t):
    size, k = IA()
    health = IA()
    attack = IA()
    alien = []
    for i in range(size):
        alien.append((health[i],attack[i]))
    alien.sort()
    low = [alien[-1][1]]
    for i in range(size - 2, -1, -1):
        if low[-1] > alien[i][1]:
            low.append(alien[i][1])
        else:
            low.append(low[-1])
    low.reverse()
    i = 0
    hit = 0
    while k > 0 and i < size:
        hit += k
        while i < size and hit >= alien[i][0]:
            i += 1
        if i >= size:
            break
        k -= low[i]


    YesNo(k > 0)