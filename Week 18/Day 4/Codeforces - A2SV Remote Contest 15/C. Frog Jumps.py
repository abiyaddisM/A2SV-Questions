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
    def helper(size):
        count = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 'R':
                count += 1
            if r + 1  >= size:
                if count == 0:
                    return False
                if nums[l] == 'R':
                    count -= 1
                l += 1

        return True

    nums = STR()
    l = 1
    r = len(nums)
    res = r + 1
    while l <= r:
        m = l + (r - l) // 2
        if helper(m):
            r = m - 1
            res = m
        else:
            l = m + 1
    print(res)
