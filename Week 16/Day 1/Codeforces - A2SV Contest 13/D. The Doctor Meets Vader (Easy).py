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

size, b =IA()

ship = IA()

base = []

for _ in range(b):
    base.append(IA())
base.sort(key= lambda x:x[0])
gold = [base[0][1]]
for i in range(1,b):
    gold.append(gold[i - 1] + base[i][1])
res = []
for s in ship:
    l = 0
    r = b - 1
    while l <= r:
        m = (r + l) // 2
        if base[m][0] > s:
            r = m - 1
        else:
            l = m + 1
    if r < 0:
        res.append(0)
    else:
        res.append(gold[r])
PA(res)