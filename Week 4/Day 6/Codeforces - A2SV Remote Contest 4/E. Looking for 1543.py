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
    n, m = IA()
    arr = []
    for __ in range(n):
        arr.append(IA())
    count = 0
    for i in range(n):
        for j in range()