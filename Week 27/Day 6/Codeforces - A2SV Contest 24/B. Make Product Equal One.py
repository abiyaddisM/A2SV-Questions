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
nums = IA()
temp = []
res = 0
for i in range(t):
    if nums[i] <= 0:
        res += abs(nums[i] + 1)
        temp.append(-1)
        continue
    res += nums[i] - 1
    temp.append(1)
neg = 0
for n in nums:
    if n < 0:
        neg += 1
if neg % 2 != 0:
    if nums.count(0) == 0:
        print(res + 2)
    else:
        print(res)
else:
    print(res)

