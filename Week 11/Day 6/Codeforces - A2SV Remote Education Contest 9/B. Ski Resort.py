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
    n, k, q = IA()
    nums = IA()
    res = 0
    l = 0
    for r in range(n):
        if nums[r] > q:
            l = r + 1
        if (r - l + 1) >= k:
            res += (r - l + 1) - k + 1

    print(res)