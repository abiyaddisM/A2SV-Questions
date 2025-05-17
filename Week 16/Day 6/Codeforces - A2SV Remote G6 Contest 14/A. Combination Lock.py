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

size = INT()
d1 = STR()
d2 = STR()
res = 0
for i in range(size):
    t1 = int(d1[i])
    t2 = int(d2[i]) 
    if t1 > t2:
        m = t2 + 10
        res += min(t1- t2,m - t1)
    else:
        m = t1 + 10
        res += min(t2 - t1, m - t2)
print(res)