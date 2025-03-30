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
nums1 = IA()
nums2 = IA()
dic = {}
res = 0
for i in range(size):
    dic[nums1[i]] = i
t = 0
for i in range(size):
    temp = dic[nums2[i]]
    if i - temp > t:
        res += (i - temp) - t
        t += 1



print(res)