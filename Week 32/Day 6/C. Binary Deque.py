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
    n, s = IA()
    a = IA()

    total = sum(a)
    if total < s:
        print(-1)
        continue
    left = 0
    cur = 0
    res = -1
    for right in range(n):
        cur += a[right]
        while cur > s and left <= right:
            cur -= a[left]
            left += 1
        if cur == s:
            res = max(res, right - left + 1)
    print(n - res if res != -1 else -1)
