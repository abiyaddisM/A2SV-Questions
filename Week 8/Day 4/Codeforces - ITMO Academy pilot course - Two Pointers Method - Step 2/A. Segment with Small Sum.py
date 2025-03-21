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
res = 0
total = 0
l = 0
for r in range(size):
    total += nums[r]
    while total > s:
        total -= nums[l]
        l += 1
    res = max(res, (r - l) + 1)
print(res)
