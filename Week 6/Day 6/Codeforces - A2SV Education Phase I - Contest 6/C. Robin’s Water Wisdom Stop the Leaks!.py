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

n, a, b = IA()
arr = IA()
s = sum(arr)
s1 = arr[0]
res = 0
arr = arr[1:]
arr.sort(reverse=True)
for ar in arr:
    if (s1 * a) / s >= b:
        print(res)
        break
    s -= ar
    res += 1
else:
    if (s1 * a) / s >= b:
        print(res)