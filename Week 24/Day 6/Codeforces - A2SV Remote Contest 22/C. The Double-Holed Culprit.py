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

size = INT()
nums = IA()

res = []

for i in range(size):
    visited = set()
    next = i
    while True:
        if next in visited:
            res.append(next + 1)
            break
        visited.add(next)
        next = nums[next] - 1



PA(res)