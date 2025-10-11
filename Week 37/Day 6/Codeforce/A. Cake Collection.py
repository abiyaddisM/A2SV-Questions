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
    for i in range(size -1, -1, -1):
        nums[i] *= k
        if k > 0:
            k -= 1
    print(sum(nums))
