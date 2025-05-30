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
    nums = STR()
    dic = Counter(nums)
    run = ['A','B','C','D','E','F','G']
    res = 0

    for r in run:
        if r not in dic:
            res += m
            continue
        if dic[r] < m:
            res += m - dic[r]
    print(res)