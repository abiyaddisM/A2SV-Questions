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
    arr = STR()
    arr += '-'
    res = set()
    l = 0
    for r in range(1,len(arr)):
        if arr[r - 1] != arr[r]:
            if (r - l) % 2 != 0:
                res.add(arr[l])
            l = r
    print(''.join(sorted(res)))