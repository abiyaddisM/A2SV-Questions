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


n, k = IA()
k -= 1
nums = []
for _ in range(n):
    nums.append(IA())
nums.sort(key= lambda x : x[0])
res = 0
total = 0
l = 0
for r in range(n):
    total += nums[r][1]
    while nums[r][0] - nums[l][0] > k:
        total -= nums[l][1]
        l += 1
    res = max(res, total)
print(res)