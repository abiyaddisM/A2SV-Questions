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

t, k = IA()
arr = IA()
arr.sort()
if k == 0 and arr[0] > 1:
    print(arr[0] - 1)
elif t == k or (t > k and arr[k - 1] != arr[k]) and k != 0:
    print(arr[k - 1])
else:
    print(-1)