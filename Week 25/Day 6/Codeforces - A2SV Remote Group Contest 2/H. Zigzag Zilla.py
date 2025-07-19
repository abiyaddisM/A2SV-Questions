from collections import Counter,deque, defaultdict
import heapq
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

n, m = IA()
res = []
state = 0
for i in range(n):
    if i % 2 == 0:
        res.append('#' * m)
    else:
        temp = ''
        if state % 2 == 1:
            temp += '#'
            temp += '.' * (m - 1)
        else:
            temp += '.' * (m - 1)
            temp += '#'
        state += 1
        res.append(temp)
for r in res:
    print(r)
