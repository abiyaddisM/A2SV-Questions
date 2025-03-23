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

def helper(color1,color2):
    if color2 == 'R':
        return color1 == 'B'
    if color2 == 'B':
        return color1 == 'G'
    if color2 == 'G':
        return color1 == 'R'
dic = {
    'R': 0,
    'B': 1,
    'G': 2
}
q = INT()
for _ in range(q):
    size, k = IA()
    arr = STR()
    if k == 1:
        print(0)
        continue
    res = size
    error = 0
    l = 1
    for r in range(1,size):
        if not helper(arr[r - 1],arr[r]):
            error += 1
        if r + 1 >= k:
            res = min(res,error)
            if not helper(arr[l - 1],arr[l]):
                error -= 1
            l += 1
    print(res)
