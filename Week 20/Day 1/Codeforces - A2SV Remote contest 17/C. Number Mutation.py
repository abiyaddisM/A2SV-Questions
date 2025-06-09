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

a, b = IA()

sb = str(b)
res = [b]
while a < b:
    if sb[-1] == '1':
        b = b - 1
        b //= 10
    elif b % 2 != 0:
        break
    else:
        b //= 2
    res.append(b)
    sb = str(b)
res.reverse()
if a == b:
    print('YES')
    print(len(res))
    PA(res)
else:
    print('NO')