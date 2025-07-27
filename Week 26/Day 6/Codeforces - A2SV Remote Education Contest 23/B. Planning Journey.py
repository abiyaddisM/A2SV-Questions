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

t = INT()
for _ in range(t):
    size, k = IA()
    nums = IA()
    res = 0
    count = 0
    l = 0
    pre = False
    for r in range(size):
        if pre:
            pre = False
            continue
        if nums[r] == 1:
            count += 1
        if (r - l) >= k - 1:

            if count == 0:
                res += 1
                pre = True
                l = r + 2
                count = 0
                continue
            if nums[l] == 1:
                count -= 1
            l += 1
    print(res)
