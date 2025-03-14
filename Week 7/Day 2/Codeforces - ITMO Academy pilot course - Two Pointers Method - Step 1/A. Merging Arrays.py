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


n, m = IA()
a1 = IA()
a2 = IA()
res = []
l, r = 0, 0
while l < len(a1) or r < len(a2):
    if l < len(a1) and r < len(a2):
         if a1[l] > a2[r]:
              res.append(a2[r])
              r += 1
         else:
              res.append(a1[l])
              l += 1
    elif l < len(a1):
        res.append(a1[l])
        l += 1
    else:
        res.append(a2[r])
        r += 1

PA(res)