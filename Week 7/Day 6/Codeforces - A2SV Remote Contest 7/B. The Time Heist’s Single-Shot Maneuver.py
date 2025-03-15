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
    n, sizeM = IA()
    arr = IA()
    m = INT()
    if (m - arr[0]) < arr[0]:
        arr[0] = m - arr[0]
    state = True
    for i in range(1, len(arr)):
        temp = m - arr[i]
        if arr[i - 1] > arr[i] and arr[i - 1] > temp:
            state = False
            break
        if arr[i - 1] <= temp <= arr[i]:
            arr[i] = temp
    if state:
        print('YES')
    else:
        print('NO')
