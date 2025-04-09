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
d = 0
min = 0
for i in range(size - 1):
    if nums[i] > nums[i + 1]:
        d += 1
        min = i

if nums[-1] > nums[0]:
    d += 1
    min = size - 1
if d > 1:
    print(-1)
elif d == 0:
    print(0)
else:
    print(size - min - 1)