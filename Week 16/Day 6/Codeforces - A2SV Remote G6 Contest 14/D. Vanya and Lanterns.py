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

size, l = IA()
nums = IA()
nums.sort()
res = nums[0]
for i in range(1,size):
    res = max((nums[i] - nums[i - 1]) / 2,res)
res = max(res,l - nums[-1])
print(res)