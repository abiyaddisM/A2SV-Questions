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
    l = 0
    r = size - 1
    while l < r:
        if arr[l] == 'L' and arr[r] == 'R':
            break
        l += 1
        r -= 1
    res = 0
    for i in range(l,r + 1):
        res += nums[i]
    print(res)