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


size, k =IA()
nums = IA()
s = sum(nums)
res = size
ad = 0
ind = 0
if s < k:
    ad = (k // s) * size
    k = k % s
    if k == 0:
        print(1, ad)
        exit()
l = 0
r = 0
total = 0
while l < size:
    total += nums[r]
    while l < size and total >= k:
        if r >= l:
            if res > r - l + 1:
                res = r - l + 1
                ind = l
        else:
            if res > (size - l) + r + 1:
                res = (size - l) + r + 1
                ind = l
        total -= nums[l]
        l += 1
    r = (r + 1) % size
print(ind + 1,ad + res)