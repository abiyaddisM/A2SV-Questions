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

size, k = IA()
nums = IA()
res = 0
max,min = nums[0]
l = 0
for r in range(size):
    