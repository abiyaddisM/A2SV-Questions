from collections import Counter,deque, defaultdict
import math
import sys

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
    nums = IA()
