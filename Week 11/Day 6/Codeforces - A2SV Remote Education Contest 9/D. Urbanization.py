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


size, n1, n2 = IA()
nums = IA()
res = 0
m = min(n1,n2)
n = max(n1,n2)
nums.sort(reverse=True)
total = 0
for i in range(m + n):
    total += nums[i]
    if i == m - 1:
        res += total / m
        total = 0
res += total / n
print(res)