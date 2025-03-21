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

def helper(arr):
    l = 0
    for r in range(len(arr)):
        a1 = arr[l: r + 1]
        a2 = arr[r + 1: r + 1 + (r - l) + 1]
        a2 = a2[::-1]
        if a1 == a2:
            l = r + 1
    return l

t =INT()
for _ in range(t):
    size = INT()
    arr = STR()
    st = ''
    l = 0
    for r in range(1,len(arr) + 1):
        if r >= len(arr) or arr[r - 1] != arr[r]:
            v = r - l
            if v >= 2 and v % 2 == 0:
                st += arr[l] * 2
            elif (v > 2 and v % 2 != 0) or v == 1:
                st += arr[l]
            l = r
    arr = st
    res1 = helper(arr)
    st = arr[res1:]
    res2 = helper(st[::-1])
    st = st[:len(st) - res2]
    print(len(st))
