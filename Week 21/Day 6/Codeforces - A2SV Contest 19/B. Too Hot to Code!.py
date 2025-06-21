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
    res = 1
    count = 1
    for r in range(1, size):
        if r == size - 1 or nums[r] - nums[r - 1] > k:
            res = max(res, count + (1 if (r == size - 1 and nums[r] - nums[r - 1] <= k) else 0))
            count = 1
        else:
            count += 1
    print(size - res)

