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

t = INT()
for _ in range(t):
    size = INT()
    nums = IA()
    p = [nums[0] if nums[0] > 0 else 0]
    n = [abs(nums[-1]) if nums[-1] < 0 else 0]
    for i in range(1,size):
        padd = 0
        nadd = 0
        if nums[i] > 0:
            padd = nums[i]
        if nums[-(i + 1)] < 0:
            nadd = abs(nums[-(i + 1)])
        p.append(p[-1] + padd)
        n.append(n[-1] + nadd)
    n.reverse()
    res = []
    for i in range(size):
        res.append(n[i] + p[i])

    print(max(res))