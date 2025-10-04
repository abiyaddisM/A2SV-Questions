import sys, threading
from collections import Counter,deque, defaultdict
import heapq
import math
def INT():
    return int(sys.stdin.readline())
def IA():
    return list(map(int, sys.stdin.readline().split()))
def SA():
    return input().split()
def STR():
    return sys.stdin.readline()
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
    state = False
    temp = num
    while temp > 0:
        if temp >= 0 and temp % 2021 == 0:
            state = True
            break
        temp -= 2020

    temp = num
    while temp > 0:
        if temp >= 0 and temp % 2020 == 0:
            state = True
            break
        temp -= 2021
    YesNo(state)
