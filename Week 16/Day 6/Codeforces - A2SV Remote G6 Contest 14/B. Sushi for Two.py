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
l, r = 0, 1
state = True
res = 0
for i in range(1,size):
    if nums[i] == nums[i - 1]:
        if state:
            r += 1
        else:
            l += 1
    if nums[i] != nums[i - 1]:
        res = max(res, min(l,r) * 2)
        if state:
            l = 1
        else:
            r = 1
        state = not state
res = max(res, min(l,r) * 2)
print(res)