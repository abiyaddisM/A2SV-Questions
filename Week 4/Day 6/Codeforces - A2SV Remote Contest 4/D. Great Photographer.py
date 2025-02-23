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

n, x = IA()
s, e = 1 , 1000
for _ in range(n):
    arr = IA()
    l = min(arr)
    r = max(arr)
    s = max(l,s)
    e = min(r,e)

if e < s:
    print(-1)
elif s <= x <= e:
    print(0)
elif x > e:
    print(x - e)
else:
    print(s - x)