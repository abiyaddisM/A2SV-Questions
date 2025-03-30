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
    res = 0
    total = 0
    l = 0
    for r in range(size):
        total += nums[r]
        while total < 0:
            total -= nums[l]
            l += 1
        res = max(res,total)
    temp = res
    # for i in range(k):
    #     temp += temp
    temp = temp * (2 ** k)
    total = sum(nums)
    print(((total - res) + temp) % (10 ** 9 + 7))
