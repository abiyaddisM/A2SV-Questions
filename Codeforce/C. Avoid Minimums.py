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
    nums = IA()
    nums.sort()
    needed = 0
    top = max(nums)
    for n in nums:
        needed += top - n
    if needed > k:
        print(-1)
        continue
    top += (k - needed) // size
    m = nums[0]
    temp = 0
    res = 0
    for n in nums:
        if n == m:
            temp += 1
        else:
            res += top - n
    if top > m:
        res += (top - m - 1) * (temp - 1)
    print(res)