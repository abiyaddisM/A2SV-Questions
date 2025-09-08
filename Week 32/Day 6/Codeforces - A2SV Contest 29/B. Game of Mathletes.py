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
    arr = IA()
    freq = [0] * (n + 1)
    for x in arr:
        if 1 <= x <= n:
            freq[x] += 1
    res = 0
    for i in range(1, n + 1):
        j = k - i
        if j < 1 or j > n:
            continue
        if i == j:
            pairs = freq[i] // 2
            res += pairs
            freq[i] -= 2 * pairs
        elif i < j:
            m = min(freq[i], freq[j])
            res += m
            freq[i] -= m
            freq[j] -= m

    print(res) 