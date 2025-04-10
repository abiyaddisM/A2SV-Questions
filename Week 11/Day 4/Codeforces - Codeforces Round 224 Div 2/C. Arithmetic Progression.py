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
dic = {}
for i in range(size - 1):
    dif = nums[i + 1] - nums[i]
    dic[dif] = dic.get(dif, 0) + 1
if len(dic) == 0:
    print(-1)
    exit()
res = []
if len(dic) == 1:
    temp = min(dic)
    res = [nums[0] - temp, nums[-1] + temp]
    if len(nums) == 2 and temp % 2 == 0:
        res.append(nums[0] + temp // 2)
        res.sort()
    ms = set(res)
    print(len(ms))
    PA(sorted(ms))
    exit()

temp = min(dic.values())
if len(dic) > 2 or temp > 1:
    print(0)
    exit()
l , r = dic.keys()
mins = l if dic[l] < dic[r] else r
maxs = l if dic[l] > dic[r] else r
if dic[l] == dic[r]:
    mins = max(dic)
    maxs = min(dic)
if mins % 2 != 0 or mins // 2 != maxs:
    print(0)
    exit()

print(1)
for i in range(size - 1):
    if nums[i + 1] - nums[i] == mins:
        print(nums[i] + maxs)
        break