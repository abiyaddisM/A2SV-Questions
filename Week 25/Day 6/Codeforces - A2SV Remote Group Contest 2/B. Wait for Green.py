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
    size, color = SA()
    size = int(size)
    nums = STR()
    pos = 0
    for i in range(size):
        if nums[i] == 'g':
            pos = i
            break
    temp = []
    for i in range(size):
        j = size - (i + 1)
        if nums[j] == 'g':
            pos = j
        temp.append(pos - j)
    temp.reverse()
    res = 0
    for i in range(size):
        if nums[i] == color:
            res = max(res, temp[i] if temp[i] >= 0 else size + temp[i])
    print(res)
