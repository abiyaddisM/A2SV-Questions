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
    size = INT()
    nums = IA()
    res = 1 + nums[0]
    for i in range(1,size):
        if nums[i] == 1:
            if nums[i - 1] == 1:
                res += 5
            else:
                res += 1
            continue
        if nums[i - 1] == 0:
            print(-1)
            break
    else:
        print(res)
