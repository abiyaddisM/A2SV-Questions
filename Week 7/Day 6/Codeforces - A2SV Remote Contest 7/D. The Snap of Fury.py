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

n = INT()
arr =  IA()
arr.reverse()
res = 0
count = 0
for i in range(n):
    count -= 1
    if count < 0:
        res += 1
    if arr[i] > count:
        count = arr[i]
print(res)