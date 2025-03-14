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

n, m = IA()
arr1 = IA()
arr2 = IA()
res = []
j = 0
for i in range(len(arr2)):

    while j < len(arr1) and arr1[j] < arr2[i]:
        j += 1
    res.append(j)

PA(res)
