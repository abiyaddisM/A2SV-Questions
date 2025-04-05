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
res = 0
temp = sorted(nums)
dic = {}
l = 0
m = 0
for r in range(size):
    dic[nums[r]] = dic.get(nums[r], 0) + 1
    while l < size and temp[l] in dic:
        if l == r:
            res += 1
        dic[temp[l]] -= 1
        if dic[temp[l]] == 0:
            dic.pop(temp[l])
        l += 1

print(res)