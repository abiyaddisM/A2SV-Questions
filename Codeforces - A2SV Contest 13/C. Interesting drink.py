from collections import Counter,deque
import math
def INT():
    return int(input())
def IA():
    return list(map(int,input().strip().split()))
def SA():
    return input().split()
def STR():
    return input()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')


size = INT()
nums = IA()
nums.sort()
t = INT()
for _ in range(t):
    day = INT()
    l = 0
    r = size - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] > day:
            r = m - 1
        else:
            l = m + 1
    if l >= size or nums[l] != day:
        print(l)
    else:
        print(l + 1)
