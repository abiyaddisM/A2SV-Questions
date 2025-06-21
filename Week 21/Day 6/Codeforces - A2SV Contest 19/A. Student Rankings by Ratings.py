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
nums2 = sorted(nums, reverse=True)
dic = {}
for i in range(len(nums2)):
    if nums2[i] not in dic:
        dic[nums2[i]] = i + 1
res = []
for n in nums:
    res.append(dic[n])
PA(res)