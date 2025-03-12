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

def find(a):
    if arr[a] != a:
        arr[a] = find(arr[a])
    return arr[a]
n, q = IA()
arr = [i for i in range(n)]
for _ in range(q):
    type, a, b = IA()
    if type == 1:
        f = find(a - 1)
        s = find(b - 1)
        if f != s:
            arr[s] = f
    elif type == 2:
        for i in range(a, b):
            f = find(a - 1)
            s = find(i)
            if f != s:
                arr[s] = f
    else:
        if find(a - 1) == find(b - 1):
            print('YES')
        else:
            print('NO')
