from collections import Counter
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

size, s = IA()
nums = IA()
res = size + 1
total = 0
l = 0
for r in range(size):
    total += nums[r]
    while total >= s:
        res = min(res, (r - l) + 1)
        total -= nums[l]
        l += 1
if res == size + 1:
    print(-1)
else:
    print(res)
