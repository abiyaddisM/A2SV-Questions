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

size = INT()
nums = IA()

pre2 = 0
pre1 = abs(nums[0] - nums[1])
for i in range(2, size):
    cur = min(pre2 + abs(nums[i] - nums[i - 2]), pre1 + abs(nums[i] - nums[i - 1]))
    pre2, pre1 = pre1, cur
print(pre1)