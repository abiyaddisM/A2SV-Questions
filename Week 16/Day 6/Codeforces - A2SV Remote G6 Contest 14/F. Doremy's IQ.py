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
    def helper(days):
        count = 0
        for n in nums:
            if n > days:
                count += 1
    size, smart = IA()
    nums = IA()
    l = 1
    r = size
    while l <= r:
        m = l + (r - l) // 2
        temp = helper(m)
        if temp[0]:
            l = m + 1
        else:
            r = m - 1
