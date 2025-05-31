from collections import Counter,deque
import bisect
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

size1, size2 = IA()
a = IA()
b = IA()
a.sort()
res = []
for n in b:
    res.append(bisect.bisect_right(a,n))
PA(res)