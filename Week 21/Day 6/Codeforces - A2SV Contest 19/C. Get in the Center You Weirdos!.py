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
    num = INT()
    res = 0
    i = 3
    count = 1
    while i <= num:
        pre = i - 2
        new = (i * i) - (pre * pre)
        res += new * count
        count += 1
        i += 2
    print(res)
