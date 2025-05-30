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
for _ in range(t):
    size = INT()
    og = IA()
    new = IA()
    dic = {}
    res = 1
    for i in range(size):
        dic[og[i]] = i
    for i in range(size - 1):
        j = -(i + 1)
        if dic[new[j]] > dic[new[j - 1]]:
            res += 1
            continue
        break

    print(size - res)

