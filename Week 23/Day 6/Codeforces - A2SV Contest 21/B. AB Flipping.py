from collections import Counter,deque, defaultdict
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
    nums = list(STR())
    res = 0
    l = 0
    for r in range(size):
        if nums[l] == 'B':
            l += 1
            continue
        if nums[r] == 'B':
            res += r - l
            nums[r] = 'A'
            l = r

    print(res)
