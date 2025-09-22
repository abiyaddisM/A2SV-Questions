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

size = INT()
word = STR()
temp = [0] * 26

for w in word[: size]:
    temp[ord(w.lower()) - 97] = 1
res = True
for t in temp:
    if not t:
        res = False
YesNo(res)
