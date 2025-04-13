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
    size = INT()
    nums = IA()
    ms = set()
    state = True
    for n in nums:
        l = n - 1
        r = n + 1
        if ms and l not in ms and r not in ms:
            state = False
        ms.add(n)
    YesNo(state)