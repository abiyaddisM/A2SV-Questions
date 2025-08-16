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

head = STR()
text = STR()

dic = Counter(head)

state = True
for t in text:
    if t == ' ':
        continue
    if t not in dic or dic[t] <= 0:
        state = False
        break
    dic[t] -= 1
YesNo(state)