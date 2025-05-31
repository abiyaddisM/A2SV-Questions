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
    def helper(money):
        count = 0
        check = (total + money) / size
        check /= 2
        state = True
        for n in nums:
            if state and n == high:
                state = False
                continue
            if check > n:
                count += 1
        return count > size // 2
    size = INT()
    nums = IA()
    total = sum(nums)
    high = max(nums)
    l = 0
    r = total * 4
    res = -1
    while l <= r:
        m = l + (r - l) // 2
        if helper(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    print(res)
