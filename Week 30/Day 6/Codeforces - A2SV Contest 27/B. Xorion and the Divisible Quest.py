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
t = min(nums)
state = True
for n in nums:
    if n % t != 0:
        state = False
        break
if state:
    print(t)
else:
    print(-1)
