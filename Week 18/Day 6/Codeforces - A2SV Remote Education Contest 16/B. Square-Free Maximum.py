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

size = INT()
nums = IA()
res = []
for n in nums:
    if n < 0:
        res.append(n)
        continue
    m = math.isqrt(n)
    if m * m != n:
        res.append(n)
print(max(res))