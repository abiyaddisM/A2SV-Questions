from collections import Counter,deque
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
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')

t = INT()
for o in range(t):
    n, m = IA()
    a = []
    b = []
    res = 0
    for __ in range(m):
        ai,bi = IA()
        a.append(ai)
        b.append(bi)
    temp = []
    for i in range(m):
        temp.append([(a[i] + (b[i] * (n-1))) / n,i])
    temp2 = sorted(a,reverse=True)
    temp.sort(reverse=True,key=lambda x:x[0])
    i = 0
    r = 0
    while r < m and n > 0:
        val = temp2[i] if i < m else -1
        if temp[r][0] >= val:
            if a[temp[r][1]] > b[temp[r][1]]:
                res += b[temp[r][1]] * n
                break
            elif n > 1:
                res += b[temp[r][1]] * (n - 1) + a[temp[r][1]]
                break
            else:
                r += 1
        else:
            res += temp2[i]
            i += 1
            n -= 1
    print(res)
    if o + 1  < t:
        input()