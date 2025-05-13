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
    n, k = IA()
    nums = IA()
    nums.sort(reverse=True)
    res = 0
    total = 0
    while res < k and total + n - nums[res] < n:
        total += n - nums[res]
        res += 1
    print(res)