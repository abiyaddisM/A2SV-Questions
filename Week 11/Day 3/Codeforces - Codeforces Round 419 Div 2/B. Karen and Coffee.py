from collections import Counter,deque
import math
def INT():
    return int(input())
def IA():
    return list(map(int,input().strip().split()))
def SA():
    return input().split()
def STR():
    return input()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')

n, k, q = IA()

diff = [0] * 200002

for i in range(n):
    l, r = IA()
    diff[l] += 1
    if r + 1 <= 200002:
        diff[r + 1] -= 1
c = [0] * 200001
c[1] = diff[1]
for i in range(2,200001):
    c[i] = c[i - 1] + diff[i]

a = [0] * (200001)
for i in range(1, 200001):
    if c[i] >= k:
        a[i] = 1
prefix = [0] * 200001
prefix[1] = a[1]
for i in range(2, 200001):
    prefix[i] = prefix[i - 1] + a[i]
for _ in range(q):
    a, b = IA()
    res = prefix[b] - (prefix[a - 1] if a > 1 else 0)
    print(res)