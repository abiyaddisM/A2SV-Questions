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
    temp = [[0 for ___ in range(m)] for __ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            state = False
            if (i > 0 and arr[i - 1][j] == arr[i][j]) or (j > 0 and arr[j - 1] == arr[i][j]):
                if