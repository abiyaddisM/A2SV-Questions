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
    size = INT()
    arr = STR()
    l = [0 for j in range(size + 1)]
    r = [0 for j in range(size + 1)]
    l[1] = 1 if arr[0] == '0' else 0
    r[1] = 1 if arr[-1] == '1' else 0
    for i in range(1,size):
        if arr[i] == '0':
            l[i + 1] += 1
        l[i + 1] += l[i]
    for i in range(2,size + 1):
        if arr[-i] == '1':
            r[i ] += 1
        r[i ] += r[i - 1]
    r.reverse()
    res = -1
    for i in range(len(l)):
        if math.ceil(i/2) <= l[i] and math.ceil((size - i) / 2) <= r[i]:
            if res == -1:
                res = i
            else:
                temp = size / 2
                res = res if abs(temp - res) <= abs(temp - i) else i

    print(res)