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


size, m = IA()
nums1 = STR()
nums2 = STR()
dic1 = Counter(nums2)
dic2 = {}
l = 0
res = 0

for r in range(size):
    dic2[nums1[r]] = dic2.get(nums1[r],0) + 1
    while (nums1[r] not in dic1 and r >= l) or dic2[nums1[r]] > dic1[nums1[r]]:
        dic2[nums1[l]] -= 1
        l += 1
    res += (r -  l) + 1
print(res)