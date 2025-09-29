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

num = INT()
res = 0
if 100 <= num:
    res += num // 100
    num = num % 100
if 20 <= num:
    res += num // 20
    num = num % 20
if 10 <= num:
    res += num // 10
    num = num % 10
if 5 <= num:
    res += num // 5
    num = num % 5
print(res + num)

