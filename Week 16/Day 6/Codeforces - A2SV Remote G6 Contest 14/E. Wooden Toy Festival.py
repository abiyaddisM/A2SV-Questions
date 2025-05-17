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
    def helper(wait):
        count = 1
        l = 0
        for r in range(size):
            if nums[r] - nums[l] > wait * 2:
                count += 1
                l = r
        return count <= 3

    size = INT()
    nums = IA()
    nums.sort()
    l = 0
    r = max(nums)
    res = 0
    while l <= r:
        m = l + (r - l) // 2
        if helper(m):
            res = m
            r = m - 1
        else:
            l = m + 1

    print(res)
