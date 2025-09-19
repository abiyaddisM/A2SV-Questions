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
nums = []
dp = [[0] * 3for _ in range(t)]
for i in range(t):
    nums.append(IA())
dp[0][0] = nums[0][0]
dp[0][1] = nums[0][1]
dp[0][2] = nums[0][2]
for i in range(1, t):
    dp[i][0] = nums[i][0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = nums[i][1] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = nums[i][2] + max(dp[i - 1][1], dp[i - 1][0])
print(max(dp[-1]))
