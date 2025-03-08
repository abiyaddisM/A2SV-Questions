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

n = INT()
a = IA()
b = IA()
res = []
for i in range(n):
    t = b.index(a[i], i, n)
    for j in range(t,i,-1):
        b[j], b[j - 1] = b[j - 1], b[j]
        res.append([j - 1, j])
print(len(res))
for r in res:
    print(r[0] + 1, r[1] + 1)