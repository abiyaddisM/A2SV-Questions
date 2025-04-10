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
    size = INT()
    nums = IA()
    arr = STR()
    pre = nums[:]
    for i in range(1,size):
        pre[i] += pre[i - 1]
    l = 0
    r = size - 1
    res = 0
    while l < r:
        if arr[l] == 'L' and arr[r] == 'R':
            res += pre[r] - (pre[l - 1] if l > 0 else 0)
            l += 1
            r -= 1
        if arr[l] != 'L':
            l += 1
        if arr[r] != 'R':
            r -= 1

    print(res)