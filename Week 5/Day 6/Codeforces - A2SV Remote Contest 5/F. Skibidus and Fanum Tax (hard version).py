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
    a = IA()
    b = IA()
    b.sort()
    j = 0
    for i in range(n - 1):
        l = a[i - 1] if i > 0 else -(10 **9)
        r = a[i + 1]
        if a[i] > r:
            while j < m:
                temp = b[j] - a[i]
                if l <= temp <= r:
                    a[i] = temp
                    break
                j += 1
        else:
            temp = b[j] - a[i]
            if temp < a[i]:
                a[i] = temp
        if j >= m:
            print('NO')
            break
    else:
        print('YES')