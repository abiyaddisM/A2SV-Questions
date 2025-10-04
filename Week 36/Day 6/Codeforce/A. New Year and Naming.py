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



n, m = IA()
s1 = SA()
s2 = SA()
q = INT()
for _ in range(q):
    index = INT()
    t1 =( index  % len(s1)) - 1
    t2 =( index % len(s2)) - 1
    print(s1[t1] + s2[t2])
