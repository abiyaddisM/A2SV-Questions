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
nums.sort()

res = []
flag = True

l = 0
r = size - 1
while l <= r:
    if flag:
        res.append(nums[l])
        l += 1
    else:
        res.append(nums[r])
        r -= 1
    flag = not flag
PA(res)