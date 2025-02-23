from collections import Counter
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

t = INT()
for _ in range(t):
    n, m = IA()
    arr = IA()
    res = []
    for __ in range(m):
        op = SA()
        l = int(op[1])
        r = int(op[2])
        maxs = 0

        for i in range(n):
            if l <= arr[i] <= r:
                if op[0] == '+':
                    arr[i] += 1
                else:
                    arr[i] -= 1
            maxs = max(maxs,arr[i])
        res.append(maxs)
    PA(res)
