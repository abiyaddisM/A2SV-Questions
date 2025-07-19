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
    size = INT()
    nums = list(STR())
    nums.pop()
    pre = []
    count = 0
    for n in nums:
        pre.append(count)
        if n == '0':
            count += 1
    nums.reverse()
    pre.reverse()
    res = [-1]
    count = int(nums[0])
    for i in range(1, size):
        spot = pre[i]
        if nums[i] == '0':
            spot += 1
        if spot >= count:
            res.append()