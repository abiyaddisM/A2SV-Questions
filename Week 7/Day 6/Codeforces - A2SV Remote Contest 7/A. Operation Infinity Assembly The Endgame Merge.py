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
    n, m, k = IA()
    a = list(STR())
    b = list(STR())
    a.sort()
    b.sort()
    res = ''
    l = 0
    r = 0
    cl = 0
    cr = 0
    while l < len(a) and r < len(b):
        if (a[l] < b[r] and cl < k) or cr == k:
            res += a[l]
            l += 1
            cl += 1
            cr = 0
        else:
            res += b[r]
            r += 1
            cr += 1
            cl = 0

    print(res)