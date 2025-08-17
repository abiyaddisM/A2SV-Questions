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
    size, qSize = IA()
    s1 = STR()
    s2 = STR()
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    pre = [0] * (size + 1)
    for i in range(size):
        temp = pre[i]
        if s1[i] != s2[i]:
            if s1[i] in dic2:
                temp-=1
                dic2[s1[i]] -= 1
                if dic2[s1[i]] == 0:
                    dic2.pop(s1[i])
            else:
                temp += 1
                dic1[s1[i]] += 1

            if s2[i] in dic1:
                temp-=1
                dic1[s2[i]] -= 1
                if dic1[s2[i]] == 0:
                    dic1.pop(s2[i])
            else:
                temp += 1
                dic2[s2[i]] += 1
        pre[i + 1] = temp
    for i in range(qSize):
        l, r = IA()
        count = max(0, abs(pre[r] - pre[l - 1]))
        if count == 0:
            print(0)
        else:
            print(count // 2)
