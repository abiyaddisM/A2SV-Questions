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
    nums = IA()
    dic = {}
    for i in range(size):
        dic[nums[i]] = i
    l = dic[1]
    r = dic[1]
    res = [0 for __ in range(size)]
    res[0] = 1
    for i in range(1,size):
        ind = dic[i + 1]
        if ind > r:
            r = ind
        elif ind < l:
            l = ind
        if r - l + 1 == i + 1:
            res[i] = 1
    print(''.join(map(str, res)))
