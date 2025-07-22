from collections import Counter, deque, defaultdict
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


t = INT()
for _ in range(t):
    size = INT()
    s = STR()

    zi = [i for i, char in enumerate(s) if char == '0']
    numz = len(zi)

    res = []
    cost = 0
    for i in range(1, size + 1):
        if i > numz:
            res.append(-1)
            continue

        tpos = size - i
        opos = zi[numz - i]

        cost += tpos - opos
        res.append(cost)

    PA(res)