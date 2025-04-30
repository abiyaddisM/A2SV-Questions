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
    n, m = IA()
    nums = []
    res = 0
    for __ in range(n):
        nums.append(IA())

    for i in range(n):
        for j in range(1, m):
            nums[i][j] += nums[i][j - 1]

    #middle = math.ceil(m / 2) if m > 1 else 0

    nums.sort(key = lambda x : x[-1], reverse = True)
    total = 0
    for i in range(n):
        for j in range(m):
            res += nums[i][j] + total
        total += nums[i][-1]
    print(res)