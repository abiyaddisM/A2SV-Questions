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

t = INT()
for _ in range(t):
    size, k = IA()
    nums = IA()
    nums.sort()
    l = 0
    r = size - 1
    res = 0
    while l < r:
        total = nums[l] + nums[r]
        if total >= k:
            r -= 1
        if total <= k:
            l += 1
        if total == k:
            res += 1
    print(res)
