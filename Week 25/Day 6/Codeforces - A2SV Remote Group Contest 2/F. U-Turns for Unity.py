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

size = INT()


s, e, p = IA()
visited = {e}
anchor = s
f = p
b = 0
for _ in range(1,size):
    s, e, p = IA()
    if s == anchor or e == anchor:
        if s == anchor:
            b += p
            anchor = e
        else:
            f += p
            anchor = s
        continue
    if e in visited:
        b += p
        visited.add(s)
        continue
    f += p
    visited.add(s)
    visited.add(e)
print(min(f,b))


