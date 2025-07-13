from collections import Counter, deque, defaultdict
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


n, k = IA()
nums = IA()
dif = []
for i in range(n - 1):
    dif.append(nums[i + 1] - nums[i])
dif.sort()
mins = 0
for i in range(n - k):
    mins += dif[i]
print(mins)