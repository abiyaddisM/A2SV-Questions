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
    n, k = IA()
    if k * 2 + 1 > n:
        print(-1)
    else:
        temp = []
        l = 1
        r = n
        t = False
        while l <= r and len(temp) < (k * 2 + 1):
            if t:
                temp.append(r)
                r -= 1
            else:
                temp.append(l)
                l += 1
            t = not t
        for i in range(l, r + 1):
            temp.append(i)
        PA(temp)