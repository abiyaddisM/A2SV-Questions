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
dic = {}
l = 0
for r in range(size):
    dic[nums[r]] = dic.get(nums[r],0) + 1
    while len(dic) > k:
        dic[nums[l]] -= 1
        if dic[nums[l]] == 0:
            dic.pop(nums[l])
        l += 1
    res += (r - l) + 1
print(res)