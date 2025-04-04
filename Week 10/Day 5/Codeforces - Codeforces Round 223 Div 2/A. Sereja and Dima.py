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


n = INT()
nums = IA()

res1 = 0
res2 = 0

flag = False

l = 0
r = n - 1
while l <= r:
    temp = max(nums[l], nums[r])
    if flag:
        res2 += temp
    else:
        res1 += temp
    flag = not flag
    if nums[l] > nums[r]:
        l += 1
    else:
        r -= 1
print(res1, res2)